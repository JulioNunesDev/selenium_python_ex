import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from destaque import highlight, dados_conta
import re

driver = webdriver.Chrome(ChromeDriverManager().install())

def test_criar_conta_A():
    
    """CRIAR CONTA A
    @web @chrome
    Feature: Criar conta A

    Scenario: Criar conta 
        Given abre o site do bankbug 
        And  aciona criar conta
        When preenche os campos necessarios
        Then procura a frase "foi criada com sucesso"
    
    """
    
    driver.get("https://bugbank.netlify.app/")
    driver.maximize_window()
    time.sleep(2)
    #Registrar uma conta
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[3]/button[2]').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[2]/input').send_keys(dados_conta()['email1'])
    
    #Preencher campo nome
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[3]/input').send_keys(dados_conta()['nome'])
    
    #Preencher campo senha e confirmação de senha
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys(dados_conta()['senha'])
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[5]/div/input').send_keys(dados_conta()['senha'])
    time.sleep(2)
    #Criar conta com saldo
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[6]/label/label').click()
    #Clicar em cadastrar
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/button').click()
    time.sleep(1)
    assertion_element = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div[2]/p')
    aux_var = assertion_element.text
    
    highlight(assertion_element, "criar_conta_A")
    assert  ("foi criada com sucesso" in str(aux_var)) == True

    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div[2]/a').click()

    """CRIAR CONTA B 
    @web @chrome
    Feature: Criar conta B

    Scenario: Criar conta 
        Given abre o site do bankbug 
        And  aciona criar conta
        When preenche os campos necessarios
        Then procura a frase "foi criada com sucesso"
    """


    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[3]/button[2]').click()
    time.sleep(2)  
    #Preencher campo email
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[2]/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[2]/input').send_keys(dados_conta()['email2'])
    
    #Preencher campo nome
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[3]/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[3]/input').send_keys(dados_conta()['nome'])
    
    #Preencher campo senha e confirmação de senha
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[4]/div/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[4]/div/input').send_keys(dados_conta()['senha'])
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[5]/div/input').clear()
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/div[5]/div/input').send_keys(dados_conta()['senha'])
    time.sleep(2)
   
    #Clicar em cadastrar
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/form/button').click()
    time.sleep(2)
    assertion_element = driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div[2]/p')
    aux_var = assertion_element.text
    
    nconta_B= re.sub('[^0-9]', '', aux_var)
    
    
    highlight(assertion_element, "criar_conta_B")
    assert  ("foi criada com sucesso" in str(aux_var)) == True
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div/div[2]/a').click()
    
    if len(nconta_B) == 4:
        numero_conta= {'conta':(str(nconta_B[0:3])),
                       'digito': (str(nconta_B[-1]))
                    }
    if len(nconta_B) == 3:
        numero_conta= {'conta':(str(nconta_B[0:2])),
                       'digito': (str(nconta_B[-1]))
                    }
       

    """TRANSFERENCIA DE A PARA B
    @web @chrome
    Feature: Transferênccia

    Scenario: Transferir 500 reais da Conta A para a Conta B
        Given faz o login na conta A
        And  abre a trasnferênci
        When preenche os campos necessarios
        Then  aparecew a mensagem "Transferencia realizada com sucesso"
    
    """

    #email
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[1]/input').send_keys(dados_conta()['email1'])
    time.sleep(1)
    #senha
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[2]/div/input').send_keys(dados_conta()['senha'])
    time.sleep(1)
    #entrar
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[3]/button[1]').click()
    time.sleep(3)
    #atual Saldo
    time.sleep(2)
    #transferencia
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[2]/div[1]/a/span/img').click()
    time.sleep(2)
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/div[1]/div[1]/input').send_keys(numero_conta['conta'])
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/div[1]/div[2]/input').send_keys(numero_conta['digito'])
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/div[2]/input').send_keys(500)
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/div[3]/input').send_keys('test_bootcamp')
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[3]/form/button').click()
    time.sleep(1)
    
    assertion_element = driver.find_element(By.XPATH,'/html/body/div/div/div[5]/div/div[2]/p')
    aux_var = assertion_element.text
    highlight(assertion_element, "transferencia_de_A_to_B")
    
    assert "Transferencia realizada com sucesso" == aux_var
    
    driver.find_element(By.XPATH,'/html/body/div/div/div[5]/div/div[2]/a').click()
    time.sleep(1)
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/a').click()
    time.sleep(1)

    driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/a').click()
    #email
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[1]/input').send_keys(dados_conta()['email2'])
    time.sleep(1)
    #senha
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[2]/div/input').send_keys(dados_conta()['senha'])
    time.sleep(1)
    #entrar
    driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[1]/form/div[3]/button[1]').click()
    time.sleep(2)
    saldo=driver.find_element(By.XPATH,'/html/body/div/div/div[3]/div[1]/p/span')
    
    highlight(saldo, "saldo_conta_B")
    
    assert saldo.text == "R$ 1.500,00"
    driver.quit()