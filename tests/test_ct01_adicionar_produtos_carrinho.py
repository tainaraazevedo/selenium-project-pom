
import pytest
from pages.carrinho_page import CarrinhoPage
from pages.home_page import HomePage
from pages.login_page import LoginPage


@pytest.mark.usefixtures("setup_teardown")
@pytest.mark.carrinho
@pytest.mark.smoke
class TestCT01:
    def test_ct01_adicionar_produtos_carrinho(self):
        login_page = LoginPage()
        home_page = HomePage()
        carrinho_page = CarrinhoPage()


        # fazer login
        login_page.fazer_login("standard_user", "secret_sauce")

        # adicionando a mochila ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Backpack")

        # verificando que a mochila foi adicionada
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")

        # clicando para voltar para a tela de produtos
        #driver.find_element(By.XPATH,"//*[@class='btn_secondary' and text()='Continue Shopping']").click()
        carrinho_page.clicar_continuar_comprando()

        # adicionar mais um produto ao carrinho
        home_page.adicionar_ao_carrinho("Sauce Labs Bolt T-Shirt")

        # verificando que os 2 produtos estao no carrinho
        home_page.acessar_carrinho()
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Backpack")
        carrinho_page.verificar_produto_carrinho_existe("Sauce Labs Bolt T-Shirt")

        #driver.find_element(By.XPATH,"//*[@class='btn_action checkout_button' and text()='CHECKOUT']").click()

        # fazendo login
        # driver.find_element(By.ID,"user-name").send_keys("standard_user")
        # driver.find_element(By.ID,"password").send_keys("secret_sauce")
        # driver.find_element(By.ID,"login-button").click()
        #
        #
        # driver.find_element(By.ID,"first-name").send_keys("TAINARA")
        # driver.find_element(By.ID, "last-name").send_keys("AZEVEDO")
        # driver.find_element(By.ID, "postal-code").send_keys("94950-080")
        # driver.find_element(By.XPATH, '//*[@id="checkout_info_container"]/div/form/div[2]/input').click()
        # driver.find_element(By.XPATH,'//*[@id="checkout_summary_container"]/div/div[2]/div[8]/a[2]').click()
        # assert driver.find_element(By.XPATH,"//*[@class='complete-header' and text()= 'THANK YOU FOR YOUR ORDER']")
