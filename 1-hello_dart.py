import numpy as np
import dartpy as dart

def main():
    viewer = dart.gui.osg.Viewer()

    # Lesson 1 Get Familiar with the DART Viewer

    # Lesson 2 Create a world and a WorldNode

    world = dart.simulation.World()

    node = dart.gui.osg.RealTimeWorldNode(world)

    viewer.addWorldNode(node)

    # Lesson 3 Create a box-shaped rigid body

    skeleton = dart.dynamics.Skeleton()

    jointAndBody = skeleton.createFreeJointAndBodyNodePair()

    body = jointAndBody[1]

    shape = dart.dynamics.BoxShape([0.3,0.3,0.3])

    body.createShapeNode(shape)

    shapenode = body.getShapeNode(0)
    shapenode.createVisualAspect()
    shapenode.createCollisionAspect()
    shapenode.createDynamicsAspect()

    world.addSkeleton(skeleton)

    viewer.addInstructionText('Welcome to the hello_dart tutorial!')
    print(viewer.getInstructions())
    viewer.setUpViewInWindow(1500, 400, 640, 480)

    viewer.setCameraHomePosition([2.57,3.14,1.64],
                                 [0.00,0.00,0.00],
                                 [-0.24,-0.25,0.94])
    
    viewer.run()

if __name__== "__main__":
    main()
