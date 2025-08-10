import conftest
from selenium.webdriver.common.by import By

from pages.base_page import BasePage


class LoginPage(BasePage):

    def __init__(self):
        super().__init__()
        self.driver = conftest.driver
        self.username_field = (By.ID,"user-name")
        self.password_field = (By.ID,"password")
        self.login_button = (By.ID,"login-button")
        self.error_message_login = (By.XPATH, "/html/body/div[2]/div[1]/div/div/form/h3")

    def fazer_login(self,usuario, senha):

        self.escrever(self.username_field, usuario)
        self.escrever(self.password_field, senha)
        self.clicar(self.login_button)

    def verificar_mensagem_erro_login_existe(self):
        self.verificar_se_elemento_exixte(self.error_message_login)

    def verificar_texto_mensagem_erro_login(self, texto_esperado):
        texto_encontrado = self.pegar_texto_elemento(self.error_message_login)
        assert texto_encontrado == texto_esperado, f"O texto encontrado foi '{texto_encontrado}', mas o texto esperado era '{texto_esperado}'."


