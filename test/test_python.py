
import FbxCommon

def display(node, indent):
  if not node: return

  print("%s%s" % (indent, node.GetNodeAttribute()))
  for i in range(node.GetChildCount()):
    child = node.GetChild(i)
    attr_type = child.GetNodeAttribute().GetAttributeType()

    print("The number of vertices is: ")
    print(child.GetMesh().GetPolygonVertexCount())#Function that counts the vertices in each face of the cube

    if attr_type == FbxCommon.FbxNodeAttribute.eMesh:
      print(child)

    display(child, indent + "  ")


sdk_manager, scene = FbxCommon.InitializeSdkObjects()

if not FbxCommon.LoadScene(sdk_manager, scene, "Cube_Elio.fbx"):
  print("error in LoadScene")

display(scene.GetRootNode(), "")

