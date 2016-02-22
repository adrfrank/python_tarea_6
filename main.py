
import wx
from wx_tarea_6 import MainForm,AddForm
from tareas import Tarea, AdministradorTareas


class FormularioPrincipal(MainForm):
	db = AdministradorTareas()
	def __init__(self,parent):
		MainForm.__init__(self,parent)
		self.Bind(wx.EVT_BUTTON, self.btnAgregar_onClick, self.btnAgregar)
		self.Bind(wx.EVT_BUTTON, self.btnEliminar_onClick, self.btnEliminar)
		self.Bind(wx.EVT_BUTTON, self.btnModificar_onClick, self.btnModificar)
		self.gridTareas.SetColLabelValue(0, 'Id')
		self.gridTareas.SetColLabelValue(1, 'Completado')
		self.gridTareas.SetColLabelValue(2, 'Nombre')
		self.fillGrid()
		self.Show()
	def fillGrid(self):
		tareas = self.db.ObtenerTodos()
		row = 0
		rowstodelete = self.gridTareas.GetNumberRows()
		if rowstodelete != 0:
			self.gridTareas.DeleteRows(numRows = rowstodelete )
		self.gridTareas.AppendRows(len(tareas))
		for t in tareas:
			self.gridTareas.SetCellValue(row,0,str(t.Id))
			self.gridTareas.SetCellValue(row,1,"Si" if t.Completado == 1 else "No")
			self.gridTareas.SetCellValue(row,2,str(t.Nombre))
			row += 1
		
		pass
	def btnAgregar_onClick(self,event):
		print "Agregar tarea"
		self.addForm = AgregarTareaForm(self,self.db)
		pass
	def btnEliminar_onClick(self,event):
		print "Eliminar tarea"
		rows = self.gridTareas.GetSelectedRows()
		if len(rows) > 0:
			dlg = wx.MessageDialog(self,'Seguro que desa eliminar las tareas', 'Confirmar', 
	            wx.YES_NO | wx.ICON_INFORMATION) 
			result = dlg.ShowModal() == wx.ID_YES
			dlg.Destroy()
			if(result == True):
				
				for row in rows:
					id = self.gridTareas.GetCellValue(row,0)
					self.db.Eliminar(int(id))
					self.fillGrid()
		pass
	def btnModificar_onClick(self,event):
		print "Modificar tarea"
		rows = self.gridTareas.GetSelectedRows()
		if len(rows) > 0:
			for row in rows:
				self.editarTarea = EditarTareaForm(self,self.db,self.gridTareas.GetCellValue(row,0))			
		pass
	def gridTareasOnGridCellLeftDClick( self, event ):
		print "doble click"
		pass
	pass

class AgregarTareaForm(AddForm):
	def __init__(self,parent,db):
		AddForm.__init__(self,parent)
		self.db = db
		self.Show()
		self.parent = parent	
		pass
		# Virtual event handlers, overide them in your derived class
	def btnCancelarOnButtonClick( self, event ):
		self.Close()
	
	def btnGuardarOnButtonClick( self, event ):
		t = Tarea()
		t.Nombre = self.txtNombre.GetValue()
		t.Completado = self.chkCompletado.GetValue()
		self.db.Agregar(t)
		#dlg = wx.MessageDialog(self, "Agregado","Agregado",wx.OK  | wx.ICON_QUESTION)
		#dlg.ShowModal()
		self.parent.fillGrid()
		self.Close()
	pass

class EditarTareaForm(AddForm):
	def __init__(self,parent,db,id):
		AddForm.__init__(self,parent)
		self.db = db
		self.Show()
		self.parent = parent	
		self.tarea = db.Obtener(int(id))
		self.txtNombre.SetValue(self.tarea.Nombre)
		self.chkCompletado.SetValue(self.tarea.Completado)
		pass
		# Virtual event handlers, overide them in your derived class
	def btnCancelarOnButtonClick( self, event ):
		self.Close()
	
	def btnGuardarOnButtonClick( self, event ):
		self.tarea.Nombre = self.txtNombre.GetValue()
		self.tarea.Completado = self.chkCompletado.GetValue()
		self.db.Editar(self.tarea)
		#dlg = wx.MessageDialog(self, "Agregado","Agregado",wx.OK  | wx.ICON_QUESTION)
		#dlg.ShowModal()
		self.parent.fillGrid()
		self.Close()


def main():
	print "Iniciando"
	app = wx.App(False)
	p = FormularioPrincipal(None)
	app.MainLoop()
	pass


if __name__ == "__main__":
	main()