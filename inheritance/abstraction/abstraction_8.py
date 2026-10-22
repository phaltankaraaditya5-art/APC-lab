from abc import ABC, abstractmethod

class Authentication(ABC):
    @abstractmethod
    def authenticate(self):
        pass


class PasswordAuth(Authentication):
    def authenticate(self):
        print("Authenticated using Password")


class OTPAuth(Authentication):
    def authenticate(self):
        print("Authenticated using OTP")


class BiometricAuth(Authentication):
    def authenticate(self):
        print("Authenticated using Biometric")


auth_methods = [PasswordAuth(), OTPAuth(), BiometricAuth()]

for method in auth_methods:
    method.authenticate()