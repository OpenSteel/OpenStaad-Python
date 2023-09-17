from comtypes import automation
from comtypes import client
import ctypes
# from comtypes import npsupport
# import numpy as np

def make_safe_array_double(size): 
    return automation._midlSAFEARRAY(ctypes.c_double).create([0]*size)
def make_safe_array_int(size): 
    return automation._midlSAFEARRAY(ctypes.c_int).create([0]*size)
def make_safe_array_long(size): 
    return automation._midlSAFEARRAY(ctypes.c_long).create([0]*size)

def make_variant_vt_ref(obj, var_type):
    var = automation.VARIANT()
    var._.c_void_p = ctypes.addressof(obj)
    var.vt = var_type | automation.VT_BYREF
    return var

os = client.GetActiveObject("StaadPro.OpenSTAAD")

geometry = os.Geometry
property = os.Property

geometry._FlagAsMethod("GetLastNodeNo")
geometry._FlagAsMethod("GetNodeCoordinates")
geometry._FlagAsMethod("GetNodeCount")
geometry._FlagAsMethod("GetNodeDistance")
geometry._FlagAsMethod("GetNodeIncidence")
geometry._FlagAsMethod("GetNodeIncidence_CIS2")
geometry._FlagAsMethod("GetNodeList")
geometry._FlagAsMethod("GetNodeNumber")
geometry._FlagAsMethod("GetNoOfSelectedNodes")
geometry._FlagAsMethod("GetSelectedNodes")

def GetLastNodeNo():
    return geometry.GetLastNodeNo()

def GetNodeCoordinates(node):
    safe_n1 = make_safe_array_double(1)
    x = make_variant_vt_ref(safe_n1,  automation.VT_R8)

    safe_n2 = make_safe_array_double(1)
    y = make_variant_vt_ref(safe_n2,  automation.VT_R8)

    safe_n3 = make_safe_array_double(1)
    z = make_variant_vt_ref(safe_n3,  automation.VT_R8)

    geometry.GetNodeCoordinates(node,x,y,z)

    return (x[0],y[0],z[0])

def GetNodeCount():
    return geometry.GetNodeCount()

def GetNodeDistance(nodeA, nodeB):
    return geometry.GetNodeDistance(nodeA,nodeB)

def GetNodeIncidence(node):
    safe_n1 = make_safe_array_double(1)
    x = make_variant_vt_ref(safe_n1,  automation.VT_R8)

    safe_n2 = make_safe_array_double(1)
    y = make_variant_vt_ref(safe_n2,  automation.VT_R8)

    safe_n3 = make_safe_array_double(1)
    z = make_variant_vt_ref(safe_n3,  automation.VT_R8)

    geometry.GetNodeIncidence(node,x,y,z)

    return (x[0],y[0],z[0])

def GetNodeList():
    n_nodes = GetNodeCount()
    safe_list = make_safe_array_long(n_nodes)
    lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

    geometry.GetNodeList(lista)

    return (lista[0])

def GetNodeNumber(x,y,z):
    return geometry.GetNodeNumber(x,y,z)

def GetNoOfSelectedNodes():
    return geometry.GetNoOfSelectedNodes()

def GetSelectedNodes():
    n_nodes = GetNoOfSelectedNodes()
    safe_list = make_safe_array_long(n_nodes)
    lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

    geometry.GetSelectedNodes(lista)

    return (lista[0])

geometry._FlagAsMethod("GetBeamLength")
geometry._FlagAsMethod("GetBeamList")
geometry._FlagAsMethod("GetBeamsConnectedAtNode")
geometry._FlagAsMethod("GetCountOfBreakableBeamsAtSpecificNodes")
geometry._FlagAsMethod("GetIntersectBeamsCount")
geometry._FlagAsMethod("GetLastBeamNo")
geometry._FlagAsMethod("GetMemberCount")
geometry._FlagAsMethod("GetMemberIncidence")
geometry._FlagAsMethod("GetMemberIncidence_CIS2")
geometry._FlagAsMethod("GetMemberUniqueID")
geometry._FlagAsMethod("GetNoOfBeamsConnectedAtNode")
geometry._FlagAsMethod("GetNoOfSelectedBeams")
geometry._FlagAsMethod("GetSelectedBeams")

def GetBeamLength(beam):
    return geometry.GetBeamLength(beam)

def GetBeamList():
    beams = GetMemberCount()
    safe_list = make_safe_array_long(beams)
    lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

    geometry.GetBeamList(lista)

    return (lista[0])

def GetBeamsConnectedAtNode():
    return

def GetCountOfBreakableBeamsAtSpecificNodes():
    pass

def GetIntersectBeamsCount():
    pass

def GetLastBeamNo():
    return geometry.GetLastBeamNo()

def GetMemberCount():
    return geometry.GetMemberCount()

def GetMemberIncidence(beam):
    safe_n1 = make_safe_array_long(1)
    x = make_variant_vt_ref(safe_n1,  automation.VT_I4)

    safe_n2 = make_safe_array_long(1)
    y = make_variant_vt_ref(safe_n2,  automation.VT_I4)

    geometry.GetMemberIncidence(beam,x,y)

    return (x[0],y[0])

def GetMemberIncidence_CIS2():
    pass

def GetMemberUniqueID():
    pass

def GetNoOfBeamsConnectedAtNode():
    pass

def GetNoOfSelectedBeams():
    return geometry.GetNoOfSelectedBeams()
def GetSelectedBeams():
    n_beams = GetNoOfSelectedBeams()
    safe_list = make_safe_array_long(n_beams)
    lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)

    geometry.GetSelectedBeams(lista)

    return (lista[0])


geometry._FlagAsMethod("GetGroupEntityCount")
geometry._FlagAsMethod("GetGroupEntities")

property._FlagAsMethod("GetBeamSectionName")

def GetGroupEntityCount(group_name):
    return geometry.GetGroupEntityCount(group_name)

def GetGroupEntities(group_name):
    beams = GetGroupEntityCount(group_name)
    safe_list = make_safe_array_long(beams)
    lista = make_variant_vt_ref(safe_list,  automation.VT_ARRAY | automation.VT_I4)
    
    geometry.GetGroupEntities(group_name,lista)
    
    return lista[0]

def GetBeamSectionName(beam):
    return property.GetBeamSectionName(beam)

