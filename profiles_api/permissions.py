from rest_framework import permissions

class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to only edit their own profiles"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit his own profile or not"""
        
        if  request.method in permissions.SAFE_METHODS:
            return True
         
        
        return obj.id == request.user.id
    
class UpdateOwnStatus(permissions.BasePermission):
    """Allow users to only edit their own status"""
    
    def has_object_permission(self, request, view, obj):
        """Check user is trying to edit his own status or not"""
        
        if  request.method in permissions.SAFE_METHODS:
            return True
         
        
        return obj.user_profile.id == request.user.id
    