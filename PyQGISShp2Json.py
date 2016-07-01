from PyQt4.QtCore import QCoreApplication
from PyQt4.QtCore import *
from PyQt4.QtGui import *
from qgis.gui import*
from qgis.core import*
from qgis.utils import*
import processing

class MyDialog(QDialog):
    
    def __init__(self):
        QDialog.__init__(self)
        
#        fruit = []
#        print  fruit
#        fruit.insert(0,"sdfas")
#        fruit.insert(1,"sdgsdfgyujg")
#        print fruit[1]
        
        self.setFixedWidth(600)
        self.setFixedHeight(350)
        
        self.textedit1=QLineEdit()
        self.textedit2=QLineEdit()
        self.textedit3=QTextEdit()
#        self.texteditOutput1=QLineEdit()
        self.texteditOutput2=QLineEdit()
        self.texteditQuery=QLineEdit()
#        self.listCsv=QListView()
#        self.listJson1=QListView()
#        self.listJson2=QListView()
        
        
        self.textedit1.setFixedWidth(300)
        self.textedit1.setFixedHeight(30)
        button1=QPushButton("...")
        button1.setFixedWidth(30)
        button1.setFixedHeight(30)
        label1=QLabel("BoundaryInput (*.shp) :                      ")
        
        hBoxLayout1=QHBoxLayout()
        hBoxLayout1.addWidget(label1)
        hBoxLayout1.addWidget(self.textedit1)
        hBoxLayout1.addWidget(button1)
        
        
        self.textedit2.setFixedWidth(300)
        self.textedit2.setFixedHeight(30)
        button2=QPushButton("...")
        button2.setFixedWidth(30)
        button2.setFixedHeight(30)
        label2=QLabel("Population data Input (*.csv)  :          ")
        
        hBoxLayout2=QHBoxLayout()
        hBoxLayout2.addWidget(label2)
        hBoxLayout2.addWidget(self.textedit2)
        hBoxLayout2.addWidget(button2)
        
        
        self.textedit3.setFixedWidth(300)
        self.textedit3.setFixedHeight(100)
#        self.textedit3.setAcceptRichText(True)
#        self.listCsv.setFixedWidth(300)
#        self.listCsv.setFixedHeight(50)
        button3=QPushButton("...")
        button3.setFixedWidth(30)
        button3.setFixedHeight(30) 
        label3=QLabel("Data Input (*.csv) :                           ")
        
        hBoxLayout3=QHBoxLayout()
        hBoxLayout3.addWidget(label3)
#        hBoxLayout3.addWidget(self.textedit3)
        hBoxLayout3.addWidget(self.textedit3)
        hBoxLayout3.addWidget(button3)
        
        self.texteditOutput2.setFixedWidth(300)
        self.texteditOutput2.setFixedHeight(30)
#        self.listJson2.setFixedWidth(300)
#        self.listJson2.setFixedHeight(50)
        buttonOutput2=QPushButton("...")
        buttonOutput2.setFixedWidth(30)
        buttonOutput2.setFixedHeight(30)
        labelOutput2=QLabel(" Output(*.geojson) :                          ")
        
        hBoxLayoutOutput2=QHBoxLayout()
        hBoxLayoutOutput2.addWidget(labelOutput2)
        hBoxLayoutOutput2.addWidget(self.texteditOutput2)
        hBoxLayoutOutput2.addWidget(buttonOutput2)
        
        self.texteditQuery.setFixedWidth(100)
        self.texteditQuery.setFixedHeight(30)
        self.texteditQuery.setText("\"iso_a2\"='UG'")
        labelQuery=QLabel("\"[FieldName]\" = '[Value]'")
        
        hBoxLayoutQuery=QHBoxLayout()
        hBoxLayoutQuery.addWidget(labelQuery)
        hBoxLayoutQuery.addWidget(self.texteditQuery)
        
    
        buttonRun=QPushButton("Run")
        buttonRun.setFixedWidth(100)
        buttonRun.setFixedHeight(30)
        
            
       
        vBoxLayout1=QVBoxLayout()
        vBoxLayout1.addSpacing(5)
        vBoxLayout1.addLayout(hBoxLayout1)
        vBoxLayout1.addLayout(hBoxLayout2)
        vBoxLayout1.addLayout(hBoxLayout3)
        
        vBoxLayout2=QVBoxLayout()
        vBoxLayout2.addSpacing(5)
#        vBoxLayout2.addLayout(hBoxLayoutOutput1)
        vBoxLayout2.addLayout(hBoxLayoutOutput2)
        
        
        vBoxLayout=QVBoxLayout()
        vBoxLayout.addLayout(vBoxLayout1)
        vBoxLayout.addLayout(vBoxLayout2)
        vBoxLayout.addLayout(hBoxLayoutQuery)
        vBoxLayout.addWidget(buttonRun)
        
        self.setLayout(vBoxLayout)
        
        self.connect(button1, SIGNAL("clicked()"), self.openShapeFile)
        self.connect(button2, SIGNAL("clicked()"), self.openCSVFile1)
        self.connect(button3, SIGNAL("clicked()"), self.openCSVFile2)
#        self.connect(buttonOutput1, SIGNAL("clicked()"), self.saveFile1)
        self.connect(buttonOutput2, SIGNAL("clicked()"), self.saveFile2)
        self.connect(buttonRun, SIGNAL("clicked()"), self.running)
    def openShapeFile(self):
        
        
        file = QFileDialog.getOpenFileName(self, "Open ShapeFile",QCoreApplication.applicationDirPath (),"Shapefiles(*.shp)")
        
        self.textedit1.setText(file)
        
        fileShape=self.textedit1.text()
        fileInfoShape=QFileInfo(fileShape)
        fileShapeName=fileInfoShape.fileName()
        layer =QgsVectorLayer(fileShape, fileShapeName, "ogr")
    def openCSVFile1(self):
        filePathDir=self.textedit1.text()
        filePathDirInfo=QFileInfo(filePathDir)
        filePathDir=filePathDir[:len(filePathDir)-len(filePathDirInfo.fileName())]
        file = QFileDialog.getOpenFileName(None, "Open CSV File",filePathDir,"CSVfiles(*.csv)")
        self.textedit2.setText(file)
    def openCSVFile2(self):
        filePathDir=self.textedit2.text()
        filePathDirInfo=QFileInfo(filePathDir)
        filePathDir=filePathDir[:len(filePathDir)-len(filePathDirInfo.fileName())]
        file = QFileDialog.getOpenFileName(self, "Open CSV File",filePathDir,"CSVfiles(*.csv)")
        
        self.textedit3.append(file)
        
#    def saveFile1(self):
#        file = QFileDialog.getExistingDirectory(self, "Select folder to save GEOJSON File",QCoreApplication.applicationDirPath ())
#        
#        self.texteditOutput1.setText(file)
    def saveFile2(self):
        filePathDir=self.textedit2.text()
        filePathDirInfo=QFileInfo(filePathDir)
        filePathDir=filePathDir[:len(filePathDir)-len(filePathDirInfo.fileName())]
       
        file = QFileDialog.getExistingDirectory(self, "Select folder to save GEOJSON File",filePathDir)
        file+="/"
        self.texteditOutput2.setText(file)
    
    def running(self):
        ss=self.textedit3.toPlainText()
        ss2=self.texteditOutput2.text()
        n=0
        m=0
        
        for char in ss:
            n+=1
            if char=="\n":
                
                csvPath=ss[m:n-1]
                print "InputFile : "+csvPath
                m=n
                csvPathInfo=QFileInfo(csvPath)
                csvName=csvPathInfo.fileName()
                
                jsonPath2=ss2+csvName[:len(csvName)-4]+".geojson"
                print "OutputFilr2 : "+jsonPath2
                self.shp2json(self.textedit1.text(), self.texteditQuery.text(), self.textedit2.text(), csvPath, jsonPath2)
        
        csvPath= ss[m:len(ss)]
        csvPathInfo=QFileInfo(csvPath)
        csvName=csvPathInfo.fileName()
#        jsonPath1=ss1[m1:len(ss1)]
        jsonPath2=ss2+csvName[:len(csvName)-4]+".geojson"
        print "InputFile : "+csvPath
#        print "OutputFilr1 : "+jsonPath1
        print "OutputFilr2 : "+jsonPath2
        
        self.shp2json(self.textedit1.text(), self.texteditQuery.text(), self.textedit2.text(), csvPath, jsonPath2)
        
        print "Finished!!!"
        
        self.textedit3.clear()
#        self.texteditOutput1.clear()
        self.texteditOutput2.clear()
        
    def shp2json(self, BoundaryFile, BoundaryQuery, PopulationFile, datafile , OutputFileName):
        exp=BoundaryQuery
#        print exp
        fileShape=BoundaryFile
        fileInfoShape=QFileInfo(fileShape)
        fileShapeName=fileInfoShape.fileName()
        layer =iface.addVectorLayer(fileShape, fileShapeName, "ogr")
        if layer.isValid():
            subset = exp
            layer.setSubsetString(subset)

        fileCSV=PopulationFile
        fileInfoCSV=QFileInfo(fileCSV)
        fileNm=fileInfoCSV.fileName()
        if  fileCSV=="":
            return
        uri ="file:"+fileCSV+"?delimiter=%s" % (";")
#        print uri
        cvslayer =iface.addVectorLayer(uri, fileNm, "delimitedtext")
        
        if cvslayer.isValid():
            subset =exp
            cvslayer.setSubsetString(subset)
        
        joinInfo = QgsVectorJoinInfo()
        joinInfo.targetFieldName = 'name'
        joinInfo.joinFieldName = 'District'
        joinInfo.memoryCache = True
        joinInfo.joinLayerId = cvslayer.id()
#        print joinInfo.joinLayerId
        layer.addJoin(joinInfo)
#        iface.addVectorLayer(layer)
        fileGeoJsonInfo=QFileInfo(OutputFileName)
        fileGeoJsonDir=OutputFileName[:len(OutputFileName)-len(fileGeoJsonInfo.fileName())]
        fileGeoJson= fileGeoJsonDir+fileNm[:len(fileNm)-4]+".geojson"
        if  fileGeoJson=="":
            return
        
        qgis.core.QgsVectorFileWriter.writeAsVectorFormat(layer, fileGeoJson, 'utf-8', layer.crs(), 'GeoJson')
#        fileCSV=PopulationFile
#        fileInfoCSV=QFileInfo(fileCSV)
#        fileNm=fileInfoCSV.fileName()
##        iface.addVectorLayer(layer)
#        fileGeoJson= fileGeoJsonDir+fileNm[:len(fileNm)-4]+".geojson"
#        if  fileGeoJson=="":
#            return
#        fileGeoJsonInfo=QFileInfo(fileGeoJson)
#        qgis.core.QgsVectorFileWriter.writeAsVectorFormat(layer, fileGeoJson, 'utf-8', layer.crs(), 'GeoJson')
        print "Made geojson File1"
        firstRes = QgsVectorLayer(fileGeoJson,fileGeoJsonInfo.fileName(), "ogr")
        if not firstRes.isValid():
            return
        
        xMax=firstRes.extent().xMaximum()+firstRes.extent().width()*0.05
        xMin=firstRes.extent().xMinimum()-firstRes.extent().width()*0.05
        yMax=firstRes.extent().yMaximum()+firstRes.extent().width()*0.05
        yMin=firstRes.extent().yMinimum()-firstRes.extent().width()*0.05
        rect=QgsRectangle(xMin,yMin,xMax,yMax)
        
        maskLayer = QgsVectorLayer("Polygon", "mask", "memory")
        QgsMapLayerRegistry.instance().addMapLayer(maskLayer)
        feature = QgsFeature()
        feature.setGeometry( QgsGeometry.fromRect(rect) )
        maskLayer.startEditing()
        maskLayer.addFeature(feature)
        maskLayer.commitChanges()
        
        fileCSV1=datafile
        fileInfoCSV1=QFileInfo(fileCSV1)
#        print fileCSV1
        if  fileCSV1=="":
            return
        uri1 ="file:"+fileCSV1+"?delimiter=%s&xField=%s&yField=%s" % (",", "LNG", "LAT")
        
        cvslayer1 = iface.addVectorLayer(uri1, fileInfoCSV1.fileName(), "delimitedtext")
#        print cvslayer1.featureCount()
        filePath1=OutputFileName
        if  filePath1=="":
            return
        filePathInfo=QFileInfo(filePath1)
#        print filePath1
        sPath=filePathInfo.filePath()
        sName=filePathInfo.fileName()
        a=len(sPath)-len(sName)
        b=len(sName)-8
        s1=sPath[:a]
        clippedPath=s1+sName[:b]+"_Clipped.shp"
        clippedName=sName[:b]+"_Clipped.shp"
        
#        print clippedPath
        print "Start Clipping"
        processing.runalg("qgis:clip", cvslayer1, maskLayer, clippedPath)
        print "End Clipping"

#        
        voronoiPath=s1+sName[:b]+"_Voronoi.shp"
        voronoiName=sName[:b]+"_Voronoi.shp"
        clippedLayer = QgsVectorLayer(clippedPath, clippedName, "ogr")
        
        print "Start the voronoi polygons"
        processing.runalg("qgis:voronoipolygons",clippedLayer,voronoiPath)
        print "End the voronoi polygons"
        
        voronoiLayer = QgsVectorLayer(voronoiPath, voronoiName, "ogr")
        res = voronoiLayer.dataProvider().addAttributes( [ QgsField("category", QVariant.String) ] )
        if res=="False":
            return
        voronoiLayer1 = QgsVectorLayer(voronoiPath, voronoiName, "ogr")
        iter=voronoiLayer1.getFeatures()
        dissolveFieldName0=fileInfoCSV1.fileName()
        dissolveFieldNameLen=len(dissolveFieldName0)-4
        dissolveFieldName=dissolveFieldName0[:dissolveFieldNameLen]
        print dissolveFieldName
        dissolveFieldOutputName="category"
        idx1=voronoiLayer1.fieldNameIndex(dissolveFieldName)
        idx2=voronoiLayer1.fieldNameIndex(dissolveFieldOutputName)
        print idx1, idx2

        maxValue=-999999999999
        minValue=999999999999
#        print str(minValue)
        for feature in iter: 
            value1=feature.attributes()[idx1]
            if value1 !=NULL:
                maxValue=max(maxValue,value1)
                minValue=min(minValue,value1)
    

        stage=(maxValue-minValue)/5
        a1=minValue
        a2=a1+stage
        a3=a2+stage
        a4=a3+stage
        a5=a4+stage
        a6=maxValue
        count=0
        
        iter1=voronoiLayer1.getFeatures()
#        print voronoiLayer1.featureCount()
#        print str(stage),a6
#        proper=QVariant.String
        progressMessageBar = iface.messageBar().createMessage("Adding the value in category filed...")
        progress = QProgressBar()
        progress.setMaximum(voronoiLayer1.featureCount())
        progress.setAlignment(Qt.AlignLeft|Qt.AlignVCenter)
        progressMessageBar.layout().addWidget(progress)
        iface.messageBar().pushWidget(progressMessageBar, iface.messageBar().INFO)

        voronoiLayer1.startEditing()
        for feature1 in iter1:
            value1=feature1.attributes()[idx1]
            if a1 <= value1 < a2:
                proper=str(a1)+"-"+str(a2)
            elif a2 <= value1 < a3:
                proper=str(a2)+"-"+str(a3)
            elif a3 <= value1 < a4:
                proper=str(a3)+"-"+str(a4)
            elif a4 <= value1 < a5:
                proper=str(a4)+"-"+str(a5)
            elif a5 <= value1 <= a6:
                proper=str(a5)+"-"+str(a6)
            else:
                proper=""
                
            voronoiLayer1.changeAttributeValue(count, idx2, proper)
            count+=1
            progress.setValue(count)
#            print "count:", count
        iface.messageBar().clearWidgets()
            
        voronoiLayer1.commitChanges()
        voronoiLayer2 = QgsVectorLayer(voronoiPath, voronoiName, "ogr")
        dissolvePath=s1+sName[:b]+"_Dissolve.shp"
        dissolveName=sName[:b]+"_Dissolve.shp"
#        print dissolvePath
        processing.alglist("Dissolve")
        processing.alghelp("qgis:dissolve")
        
        print "Start Dissolving"
        processing.runalg("qgis:dissolve",voronoiLayer2,False,"category",dissolvePath)
        print "End Dissolving"
        
        dissolveLayer = QgsVectorLayer(dissolvePath, dissolveName, "ogr")
        
        fInfo=QFileInfo(dissolvePath)
        resultClipName=fInfo.fileName()
        resultClipPath=dissolvePath[:len(dissolvePath)-len(resultClipName)]
        
        resultClipName=resultClipName[:len(resultClipName)-4]+"Clip.shp"
        resultClipPath=resultClipPath+resultClipName
        
        print "Start Clipping"
        processing.runalg("qgis:clip", dissolveLayer, firstRes, resultClipPath)
        print "End Clipping"
        
        
        endLayer = QgsVectorLayer(resultClipPath, resultClipName, "ogr")
        
        fileGeoJson1= OutputFileName
        if  fileGeoJson1=="":
            return
        fileGeoJsonInfo1=QFileInfo(fileGeoJson1)
        qgis.core.QgsVectorFileWriter.writeAsVectorFormat(endLayer, fileGeoJson1, 'utf-8', endLayer.crs(), 'GeoJson')
        print "Made geojson File2"
        
#        jsonLayer1 = iface.addVectorLayer(fileGeoJson, fileGeoJsonInfo.fileName(), "ogr")
        jsonLayer2 = iface.addVectorLayer(fileGeoJson1, fileGeoJsonInfo1.fileName(), "ogr")
        
        
#
dlg=MyDialog()
dlg.show()

