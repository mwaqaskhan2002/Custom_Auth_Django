from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from django.db.models import Q

"""
CLASS EmailOrUsernameBackend:
    
    FUNCTION authenticate (Identity_Input, Password):
        
        1. MODEL GETTER: 
           Pehle pata karo ke project mein "User" table kaunsa hai (Custom ya Default).

        2. SEARCH IN DATABASE (Try Block):
           Database mein ek aisi entry dhoondo jahan:
           - USERNAME field match kare Identity_Input se (Case-insensitive: yani 'A' aur 'a' barabar hain)
           - YA (OR)
           - EMAIL field match kare Identity_Input se (Case-insensitive)

        3. IF NOT FOUND (Except Block):
           Agar database mein aisa koi banda nahi mila jiska Username ya Email match ho:
           - Wapas khali hath (None) bhej do.

        4. SECURITY CHECK (If condition):
           Agar banda mil gaya hai, to ab 2 cheezein check karo:
           - A: Kya (Dala gaya Password) wahi hai jo is User ka database mein save hai?
           - B: Kya is User ko login karne ki ijazat hai? (Maslan: Account active hai ya nahi?)

        5. FINAL RESULT:
           - Agar dono cheezein (Password aur Active status) sahi hain:
             - Us User ka "Object" wapas bhej do (Login Success!)
           - Agar Password galat hai:
             - Khali hath (None) bhej do (Login Fail).
"""
class EmailorUsernameModelBackend(ModelBackend):
    def authenticate(self, request, username=None, password=None, **kwargs):
        UserModel = get_user_model()
        
        try:
            user = UserModel.objects.get(
                Q(username__iexact=username) | Q(email__iexact=username)
            )
        except UserModel.DoesNotExist:
            return None 
        
        if user.check_password(password) and self.user_can_authenticate(user):
            return user #Login Success
        return None #Login Failure
