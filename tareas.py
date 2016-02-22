#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Adrian Francisco Gonzalez Gutierrez
import mysqlhelper as mysql


class Tarea():
	Id=-1
	Completado = False
	Nombre = ""
	def __str__(self):
		return "{ Id: %d, Nombre: '%s', Completado: %s }"%(self.Id,self.Nombre,self.Completado)

	def __repr__(self):
		return "{ Id: %d, Nombre: '%s', Completado: %s }"%(self.Id,self.Nombre,self.Completado)
	pass


class AdministradorTareas():
	def ObtenerTodos(self):
		sql_tareas = mysql.run_query("SELECT Id,Nombre,Completado FROM tareas")
		tareas = []
		for row in sql_tareas:
			t = Tarea()
			t.Id = row[0]
			t.Nombre = row[1]
			t.Completado = int(row[2])
			tareas.append(t)
			pass
		return tareas
	def Agregar(self,tarea):
		query = "INSERT INTO tareas(Nombre,Completado) values('%s',%d)"%(tarea.Nombre,tarea.Completado)
		#print query
		mysql.run_query(query)
		pass
	def Eliminar(self,id):
		query = "DELETE FROM tareas where Id = %d "%(id,)
		#print query
		mysql.run_query(query)
		pass
	def Obtener(self,id):
		sql_tareas = "SELECT Id,Nombre,Completado FROM tareas WHERE Id = %d"%(id,)
		res = mysql.run_query(sql_tareas)
		tarea = Tarea()
		for t in res:
			tarea.Id = t[0]
			tarea.Nombre = t[1]
			tarea.Completado = int(t[2]) 
		return tarea if tarea.Id != -1 else None
		pass
	def ImprimirTodos(self):
		print "Id\t|Completado\t|Nombre"
		print "-----------------------------------"
		tareas = self.ObtenerTodos()
		for t in tareas:
			print "%d\t| %s\t\t| %s"%(t.Id,("Si" if t.Completado == 1 else "No"),t.Nombre)
	def Editar(self,tarea):
		sql_tareas = "UPDATE tareas SET Nombre = '%s', Completado = %s WHERE Id =  %d" %(tarea.Nombre,tarea.Completado,tarea.Id)
		mysql.run_query(sql_tareas)
		pass
	pass


if __name__ == "__main__":
	at = AdministradorTareas()
	op = ""
	while op != "0":
		print "\n----------------------"
		print "TAREAS"
		print "----------------------\n"
		print "1. Agregar tarea"
		print "2. Buscar tarea"
		print "3. Modificar tarea"
		print "4. Mostrar todas las tareas"
		print "5. Eliminar tarea"
		print "0. Salir"
		op =  raw_input("\nOpción: ")
		if op == "1":
			t = Tarea()
			print "Nueva tarea:"
			t.Nombre = raw_input("Nombre: ")
			tmp = raw_input("Completado (S/N)")
			t.Completado = tmp == "S" or tmp == "s"
			at.Agregar(t);
			at.ImprimirTodos()
			pass
		elif op == "2":
			id = raw_input("Ingrese el id de la tarea a buscar: ")
			t = at.Obtener(int(id))
			if t != None:
				print "----------------------"
				print "Tarea "+str(t.Id)
				print "----------------------"
				print "Nombre: "+str(t.Nombre)
				print "Completado: "+ str(t.Completado)
				print "----------------------"
				print ""
			else:
				print "Tarea inexistente"
		elif op == "3":
			print "Modificar tarea"
			id = raw_input("Ingrese el id de la tarea a modificar: ")
			t = at.Obtener(int(id))
			if t == None:
				print "Tarea inexistente"
			else:
				tmp = raw_input("Nombre: (Anterior: "+str(t.Nombre)+") ")
				if tmp != "":
					t.Nombre = tmp
				tmp = raw_input("Completado: (Anterior: "+("S" if t.Completado == 1 else "N")+") ")
				if tmp != "": 
					t.Completado = (tmp == "S" or tmp == "s")
				at.Editar(t)
				at.ImprimirTodos()

		elif op == "4":
			at.ImprimirTodos()
		elif op == "5":
			id = raw_input("Ingrese el id de la tarea a eliminar: ")
			at.Eliminar(int(id))
			at.ImprimirTodos()
			pass
		pass

	


