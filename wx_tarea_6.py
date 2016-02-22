# -*- coding: utf-8 -*- 

###########################################################################
## Python code generated with wxFormBuilder (version Feb 16 2016)
## http://www.wxformbuilder.org/
##
## PLEASE DO "NOT" EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid

###########################################################################
## Class MainForm
###########################################################################

class MainForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Tareas - Tarea 6", pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer2 = wx.BoxSizer( wx.VERTICAL )
		
		bSizer3 = wx.BoxSizer( wx.HORIZONTAL )
		
		self.btnAgregar = wx.Button( self, wx.ID_ANY, u"Agregar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnAgregar, 0, wx.ALL, 5 )
		
		self.btnEliminar = wx.Button( self, wx.ID_ANY, u"Eliminar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnEliminar, 0, wx.ALL, 5 )
		
		self.btnModificar = wx.Button( self, wx.ID_ANY, u"Modificar", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer3.Add( self.btnModificar, 0, wx.ALL, 5 )
		
		
		bSizer2.Add( bSizer3, 0, wx.EXPAND, 5 )
		
		self.gridTareas = wx.grid.Grid( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )
		
		# Grid
		self.gridTareas.CreateGrid( 5, 3 )
		self.gridTareas.EnableEditing( False )
		self.gridTareas.EnableGridLines( True )
		self.gridTareas.EnableDragGridSize( False )
		self.gridTareas.SetMargins( 0, 0 )
		
		# Columns
		self.gridTareas.SetColSize( 0, 35 )
		self.gridTareas.SetColSize( 1, 220 )
		self.gridTareas.SetColSize( 2, 106 )
		self.gridTareas.EnableDragColMove( False )
		self.gridTareas.EnableDragColSize( False )
		self.gridTareas.SetColLabelSize( 30 )
		self.gridTareas.SetColLabelValue( 0, u"Id" )
		self.gridTareas.SetColLabelValue( 1, u"Nombre" )
		self.gridTareas.SetColLabelValue( 2, u"Completado" )
		self.gridTareas.SetColLabelValue( 3, wx.EmptyString )
		self.gridTareas.SetColLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Rows
		self.gridTareas.EnableDragRowSize( True )
		self.gridTareas.SetRowLabelSize( 80 )
		self.gridTareas.SetRowLabelAlignment( wx.ALIGN_CENTRE, wx.ALIGN_CENTRE )
		
		# Label Appearance
		
		# Cell Defaults
		self.gridTareas.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer2.Add( self.gridTareas, 1, wx.ALL|wx.EXPAND, 5 )
		
		
		self.SetSizer( bSizer2 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.gridTareas.Bind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, self.gridTareasOnGridCellLeftClick )
		self.gridTareas.Bind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, self.gridTareasOnGridCellLeftDClick )
	
	def __del__( self ):
		# Disconnect Events
		self.gridTareas.Unbind( wx.grid.EVT_GRID_CELL_LEFT_CLICK, None )
		self.gridTareas.Unbind( wx.grid.EVT_GRID_CELL_LEFT_DCLICK, None )
	
	
	# Virtual event handlers, overide them in your derived class
	def gridTareasOnGridCellLeftClick( self, event ):
		event.Skip()
	
	def gridTareasOnGridCellLeftDClick( self, event ):
		event.Skip()
	

###########################################################################
## Class AddForm
###########################################################################

class AddForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Agregar Tarea", pos = wx.DefaultPosition, size = wx.Size( 220,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 220,150 ), wx.Size( 220,150 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lblNombre = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombre.Wrap( -1 )
		fgSizer1.Add( self.lblNombre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtNombre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lblCompletado = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCompletado.Wrap( -1 )
		fgSizer1.Add( self.lblCompletado, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chkCompletado = wx.CheckBox( self, wx.ID_ANY, u"Completado", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.chkCompletado, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnCancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnGuardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnGuardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnCancelar.Bind( wx.EVT_BUTTON, self.btnCancelarOnButtonClick )
		self.btnGuardar.Bind( wx.EVT_BUTTON, self.btnGuardarOnButtonClick )
	
	def __del__( self ):
		# Disconnect Events
		self.btnCancelar.Unbind( wx.EVT_BUTTON, None )
		self.btnGuardar.Unbind( wx.EVT_BUTTON, None )
	
	
	# Virtual event handlers, overide them in your derived class
	def btnCancelarOnButtonClick( self, event ):
		event.Skip()
	
	def btnGuardarOnButtonClick( self, event ):
		event.Skip()
	

###########################################################################
## Class EditForm
###########################################################################

class EditForm ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"Editar Tarea", pos = wx.DefaultPosition, size = wx.Size( 220,150 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.Size( 220,150 ), wx.Size( 220,150 ) )
		
		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )
		
		self.lblNombre = wx.StaticText( self, wx.ID_ANY, u"Nombre", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblNombre.Wrap( -1 )
		fgSizer1.Add( self.lblNombre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.txtNombre = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.txtNombre, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.lblCompletado = wx.StaticText( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.lblCompletado.Wrap( -1 )
		fgSizer1.Add( self.lblCompletado, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.chkCompletado = wx.CheckBox( self, wx.ID_ANY, u"Completado", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.chkCompletado, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnCancelar = wx.Button( self, wx.ID_ANY, u"Cancelar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnCancelar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		self.btnGuardar = wx.Button( self, wx.ID_ANY, u"Guardar", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer1.Add( self.btnGuardar, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL|wx.ALIGN_CENTER_VERTICAL, 5 )
		
		
		self.SetSizer( fgSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.btnCancelar.Bind( wx.EVT_BUTTON, self.btnCancelarOnButtonClick )
		self.btnGuardar.Bind( wx.EVT_BUTTON, self.btnGuardarOnButtonClick )
	
	def __del__( self ):
		# Disconnect Events
		self.btnCancelar.Unbind( wx.EVT_BUTTON, None )
		self.btnGuardar.Unbind( wx.EVT_BUTTON, None )
	
	
	# Virtual event handlers, overide them in your derived class
	def btnCancelarOnButtonClick( self, event ):
		event.Skip()
	
	def btnGuardarOnButtonClick( self, event ):
		event.Skip()
	

