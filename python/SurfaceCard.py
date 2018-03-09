from Card import Card
from enum import Enum

class SurfaceCard(Card):
    """ Class for the storage of the generic SurfaceCard type
    Methods for the generation of flat geometry surface card data
    should be place here. Classes needing to write flat 
    surface card data should be implemented in its own
    CodeSurfaceCard.py file
    """
    
    surface_type = 0
    surface_id = 0
    surface_transform = 0
    surface_coefficients = []
    comment = ""
    b_box = [0,0,0,0,0,0] # b 
    
    class SurfaceType(Enum):
        PLANE_GENERAL = 0
        PLANE_X = 1
        PLANE_Y = 2
        PLANE_Z = 3
        CYLINDER_X = 4
        CYLINDER_Y = 5
        CYLINDER_Z = 6
        SPHERE_GENERAL = 7
        CONE_X = 8
        CONE_Y = 9
        CONE_Z = 10
        TORUS_X = 11
        TORUS_Y = 12
        TORUS_Z = 13
        GENERAL_QUADRATIC = 14
        MACRO_RPP = 15
        MACRO_BOX = 16
        MACRO_RCC = 17
    
    # constructor for building a surface card
    def __init__(self,card_string):
        Card.__init__(self,card_string)

    def __str__(self):
        string = "SurfaceCard: \n"
        string += "Surface ID " + str(self.surface_id)+"\n"
        string += "Transform ID " + str(self.surface_transform) + "\n"
        string += "Surface Type " + str(self.surface_type)+"\n"
        string += "Surface Coefficients " + str(self.surface_coefficients)+"\n"
        string += "Comment: " + str(self.comment)+"\n"
        return string
        
    def set_type(self, surf_id, surf_transform, surf_type, coords):
        self.surface_id = surf_id
        self.surface_transform = surf_transform
        self.surface_type = surf_type
        self.surface_coefficients = coords
        
    # test if the current surface is a macrobody or not
    def is_macrobody(self):
        if self.surface_type == self.SurfaceType['MACRO_RPP']:
            return True
        if self.surface_type == self.SurfaceType['MACRO_BOX']:
            return True
        if self.surface_type == self.SurfaceType['MACRO_RCC']:
            return True
        return False
    
    # get the bounding box 
    def bounding_box(self):
        # bounding box return value
        b_box = [0,0,0,0,0,0]

        if self.surface_type == self.SurfaceType['PLANE_X']:
            b_box[0] = self.surface_coefficients[3]
            b_box[1] = self.surface_coefficients[3]
        elif self.surface_type == self.SurfaceType['PLANE_Y']:
            b_box[2] = self.surface_coefficients[3]
            b_box[3] = self.surface_coefficients[3]
        elif self.surface_type == self.SurfaceType['PLANE_Z']:
            b_box[4] = self.surface_coefficients[3]
            b_box[5] = self.surface_coefficients[3]
        elif self.surface_type == self.SurfaceType['CYLINDER_X']:
            b_box[2] = self.surface_coefficients[0] - self.surface_coefficients[2]
            b_box[3] = self.surface_coefficients[0] + self.surface_coefficients[2]
            b_box[4] = self.surface_coefficients[1] - self.surface_coefficients[2]
            b_box[5] = self.surface_coefficients[1] + self.surface_coefficients[2]
        elif self.surface_type == self.SurfaceType['CYLINDER_Y']:
            b_box[0] = self.surface_coefficients[0] - self.surface_coefficients[2]
            b_box[1] = self.surface_coefficients[0] + self.surface_coefficients[2]
            b_box[4] = self.surface_coefficients[1] - self.surface_coefficients[2]
            b_box[5] = self.surface_coefficients[1] + self.surface_coefficients[2]
        elif self.surface_type == self.SurfaceType['CYLINDER_Z']:
            b_box[0] = self.surface_coefficients[0] - self.surface_coefficients[2]
            b_box[1] = self.surface_coefficients[0] + self.surface_coefficients[2]
            b_box[2] = self.surface_coefficients[1] - self.surface_coefficients[2]
            b_box[3] = self.surface_coefficients[1] + self.surface_coefficients[2]
        elif self.surface_type == self.SurfaceType['SPHERE_GENERAL']:
            b_box[0] = self.surface_coefficients[0] - self.surface_coefficients[3]
            b_box[1] = self.surface_coefficients[0] + self.surface_coefficients[3]
            b_box[2] = self.surface_coefficients[1] - self.surface_coefficients[3]
            b_box[3] = self.surface_coefficients[1] + self.surface_coefficients[3]
            b_box[4] = self.surface_coefficients[2] - self.surface_coefficients[3]
            b_box[5] = self.surface_coefficients[2] + self.surface_coefficients[3]
        return b_box
