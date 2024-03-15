from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC

service = Service(executable_path='C:\\Users\\LabInfo\\Documents\\teste.2\\TesteSelenium_heroku-main\\chromedriver.exe')
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

try:
    driver.get("https://github.com/login")
    
    print("1")
    def enviarDados(usuario, senha):
        email_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "login_field"))
        )
        print("2")
        senha_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "password"))
        )
        print("3")
        btn_login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="login"]/div[4]/form/div/input[13]'))
        )
        print("4")
        email_login.clear
        senha_login.clear
        email_login.send_keys(usuario)
        senha_login.send_keys(senha)
        btn_login.click()
        driver.implicitly_wait(5)  
        btn_reposi = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[6]/div/div/aside/div/div/loading-context/div/div[1]/div/ul/li[1]/div/div/a'))
        )
        btn_reposi.click()
    print("5")
    alert = enviarDados("luisaalvim","061206luisa")
    if 'You logged into a secure area' in alert:
        print("Teste de login bem sucedido")
    else:
        print("Falaha ao efetuar login, teste falhou")

    print("Todos os testes concluídos com sucesso!")

except:
    print("Teste Falhou! Erro na execução")


driver.quit()