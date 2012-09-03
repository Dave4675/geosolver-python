from includes import *
from ui_compositionView import Ui_compositionView
#from tree import Tree
from cvitems import CVCluster, CVConnection
from parameters import Settings
import random
import geosolver.graph
import numpy

class DecompositionView(QtGui.QDialog):
    """ A view where the decomposition of the system of constraints is visualised as a directed acyclic graph"""
    def __init__(self, viewport, viewportMngr, vpType, prototypeMngr, parent=None):
        """ Initialization of the CompositionView class
            
        Parameters:
            viewportMngr - the manager of the viewports where the composition view can reside in
            prototypeMngr - the manager of the prototypes is used to obtain the results of the solver
        """
        QtGui.QDialog.__init__(self, parent)
        self.prototypeManager = prototypeMngr
        self.viewport = viewport
        self.viewportManager = viewportMngr
        self.settings = Settings()
        self.setWindowFlags(QtCore.Qt.Window)
        self.timer = QtCore.QObject()

        """map GeometricDecomposition to CVCluster"""
        self.map = {}
        
        self.ui = Ui_compositionView()
        self.ui.setupUi(self)
        self.ui.graphicsView.setupViewport(QtOpenGL.QGLWidget(QtOpenGL.QGLFormat(QtOpenGL.QGL.SampleBuffers|QtOpenGL.QGL.DoubleBuffer)))
        self.ui.graphicsView.setRenderHints(QtGui.QPainter.Antialiasing | QtGui.QPainter.SmoothPixmapTransform)
        
        self.currentTool = None
        self.viewportType = vpType
        self.orientation = TreeOrientation.BOTTOM

        self.overConstrainedColor = QtGui.QColor(0,0,255)
        self.underConstrainedColor = QtGui.QColor(255,0,0)
        self.wellConstrainedColor = QtGui.QColor(0,255,0)
        self.unsolvedColor = QtGui.QColor(125,124,255)
        
        self.createScene()
        self.createTriggers()
        
    def createTriggers(self):
        """ Create the triggers for the components in the graphical window """ 
        QtCore.QObject.connect(self.ui.zoomInButton,QtCore.SIGNAL("clicked()"),self.zoomIn)
        QtCore.QObject.connect(self.ui.zoomOutButton,QtCore.SIGNAL("clicked()"),self.zoomOut)
        QtCore.QObject.connect(self.ui.fitButton, QtCore.SIGNAL("clicked()"), self.fit)
        #QtCore.QObject.connect(self.ui.collapseButton, QtCore.SIGNAL("clicked()"), self.collapse)
        QtCore.QObject.connect(self.ui.graphicsScene, QtCore.SIGNAL("changed(const QList<QRectF> & )"), self.updateSceneRect)
        QtCore.QObject.connect(self.ui.verticalSlider,QtCore.SIGNAL("valueChanged(int)"),self.setupMatrix)
        #QtCore.QObject.connect(self.settings.dvData,QtCore.SIGNAL("treeOrientationChanged()"), self.updateTreeOrientation)
             
    def getViewportType(self):
        return self.viewportType
        
    def updateGL(self):
        self.update()
    
    def createDecomposition(self):
        """ Create a new decomposition. If an older one exists it will be removed. """ 
        self.clearScene()
        self.createScene()
       
    def clearScene(self):
        self.map = {}
        if self.ui.graphicsScene != None:
            for item in self.ui.graphicsView.items():
                item.hide()
                if item.parentItem() == None:
                    self.ui.graphicsScene.removeItem(item)
            
    def createScene(self):
        """ Updating the view with new data and nodes for the visualisation of the tree """
        if self.prototypeManager.result != None:
            # get all clusters from result
            new = [self.prototypeManager.result]
            clusters = set()
            while len(new) > 0:
                c = new.pop()
                clusters.add(c)
                for child in c.subs:
                    if child not in clusters:
                        new.append(child)
            # create N layers for clusters with 1-N variables
            N = len(self.prototypeManager.result.variables)
            layers = []
            for n in range(0,N+1):
                layers.append([])
            # add clusters to layers 
            for c in clusters:
                n = len(c.variables)
                layers[n].append(c)
            # sort clusters in layers
            # ?? 
            # map GeometricDecompositions to CVClusters
            for n in range(0,N+1):
                layer = layers[n]
                for k in range(0,len(layer)):
                    c = layer[k]
                    y = n * 50.0
                    x = (k - len(layer)/2.0) * 50.0 * n
                    cvcluster = CVCluster(self, c, x,y)
                    self.ui.graphicsScene.addItem(cvcluster)
                    self.map[c] = cvcluster
                    self.map[cvcluster] = c
            # add CVConnections
            for c in clusters:
                for child in c.subs:
                    self.ui.graphicsScene.addItem(CVConnection(self, self.map[c], self.map[child]))
            # iteratively improve graph layout
            # self.optimiseGraphLayout()

    def optimiseGraphLayout(self):

        # create a graph of clusters and connections
        graph = geosolver.graph.Graph()
        if self.ui.graphicsScene != None:
            for item in self.ui.graphicsView.items():
                if isinstance(item, CVCluster):
                    graph.add_vertex(item)
                    item.force = numpy.array([0.0,0.0])
                elif isinstance(item, CVConnection):
                    graph.add_edge(item.nodeFrom, item.nodeTo, item)   
       
        l = list(graph.vertices())

        # iteratively implove layout 
        for i in range(100):
            # clear forces 
            for c in l:
                c.force = numpy.array([random.random()*0, random.random()*0])

            # determine forces due to overlapping cluster boxes
            n = len(l)
            for i in range(n):
                for j in range(i+1,n):
                    c1 = l[i]     
                    c2 = l[j] 
                    box1 = c1.paintRect.translated(c1.position)
                    box1.setWidth(2*box1.width())
                    box1.setHeight(2*box1.height())
                    box2 = c2.paintRect.translated(c2.position)
                    box2.setWidth(2*box2.width())
                    box2.setHeight(2*box2.height())
                    #print "box 1", box1 
                    #print "box 2", box2 
                    if box1.intersects(box2):
                        #print "intersects"
                        force = box1.intersected(box2).width() + box1.intersected(box2).height() 
                        centerdiff = box2.center()-box1.center()
                        direction = numpy.array([centerdiff.x(),centerdiff.y()])
                        norm =  numpy.linalg.norm(direction)
                        if norm != 0:
                            direction = direction / numpy.linalg.norm(direction)
                        #direction[1] = 0.0
                        c1.force += -force*direction / 10.0;
                        c2.force += force*direction / 10.0;
                        #print "force 1", c1.force
                        #print "force 2", c2.force
            
            # determine forces due to connections
            for e in graph.edges():
                c1 = e[0]     
                c2 = e[1] 
                box1 = c1.paintRect.translated(c1.position)
                box2 = c2.paintRect.translated(c2.position)
                centerdiff = box2.center()-box1.center()
                direction = numpy.array([centerdiff.x(),centerdiff.y()])
                norm =  numpy.linalg.norm(direction)
                if norm != 0:
                    direction = direction / numpy.linalg.norm(direction)
                goal = box1.height() + box2.height() + box1.width() + box2.width()
                force = (norm - goal) / 20.0
                #direction[1] = 0.0
                c1.force += +force*direction;
                c2.force += -force*direction;
                #print "force ", force

            # apply forces 
            for c in l:
                move = QtCore.QPointF(c.force[0],c.force[1])
                c.position += move
                c.translate(move.x(), move.y())
        # done iterating

        # uppate connectors
        for e in graph.edges():
            connector = graph.get(e[0],e[1])
            connector.determinePath()

    def updateViewports(self):
        self.viewportManager.updateViewports()
    
    def updateSceneRect(self, rectList=None):
        self.ui.graphicsScene.setSceneRect(self.ui.graphicsScene.itemsBoundingRect())
    
    def zoomIn(self):
        """ Zoom in the graphics view, by updating the vertical slider """
        self.ui.verticalSlider.setValue(self.ui.verticalSlider.value() + 1)
    
    def zoomOut(self):
        """ Zoom out the graphics view, by updating the vertical slider """
        self.ui.verticalSlider.setValue(self.ui.verticalSlider.value() - 1)
    
    def fit(self):
        """ Fits the tree exactly in the graphics view """
        self.ui.graphicsView.fitInView(0.0, 0.0, self.ui.graphicsScene.width(), self.ui.graphicsScene.height(), QtCore.Qt.KeepAspectRatio)
        """ Update the slider """
        value = (math.log(self.ui.graphicsView.matrix().m11(),2)*50) + 250.0
        self.ui.verticalSlider.setValue(value)
    
    def setupMatrix(self, value):
        """ Zoom in/out the graphics view, depending on the value of the slider 
        
        Parameters
            value    -    value of the updated slider
        """
        scale = math.pow(2.0, (self.ui.verticalSlider.value()-250.0)/50.0)
        matrix = QtGui.QMatrix()
        matrix.scale(scale,scale)

        self.ui.graphicsView.setMatrix(matrix)
