import conftest


class BasePage:
    def __init__(self):
        self.driver = conftest.driver

    def encontrar_elemento(self,locator):
        return self.driver.find_element(*locator)

    def encontrar_elementos(self,locator):
        return self.driver.find_elements(*locator)

    def escrever(self, locator, text):
        self.encontrar_elemento(locator).send_keys(text)

    def clicar(self, locator):
        self.encontrar_elemento(locator).click()


    def verificar_se_elemento_exixte(self, locator):
        assert self.encontrar_elemento(locator).is_displayed(), f"o elemento '{locator}'nao foi encontrado na tela."

    def pegar_texto_elemento(self, locator):
        return self.encontrar_elemento(locator).text



