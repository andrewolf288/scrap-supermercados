from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time

# Funcion para seleccionar el supermercado
def seleccionarSupermercado(driver):
    print('Seleccionar supermercado')
    select_supermercado = driver.find_element(by=By.ID, value="url")
    select = Select(select_supermercado)
    select.select_by_value("6")
    boton_ingresar = driver.find_element(by=By.XPATH, value='//*[@id="form"]/div[2]/input')
    boton_ingresar.click()

def loginUsuario(driver):
    print('Logearse')
    input_username = driver.find_element(by=By.ID, value='username')
    input_username.send_keys("ventas@emaransac.com")
    input_password = driver.find_element(by=By.ID, value='password')
    input_password.send_keys("ventas@1234")
    input_submit = driver.find_element(by=By.ID, value='kc-login')
    input_submit.click()

def seleccionarMenu(driver):
    print('Seleccionar menu')
    menu_abastecimiento = driver.find_element(by=By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[1]/div/div/div[3]/div/span[3]')
    menu_abastecimiento.click()
    menu_indicadores = driver.find_element(by=By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670-overlays"]/div[2]/div/div/span[1]')
    menu_indicadores.click()

def generarInforme(driver):
    print('Generar informe')
    boton_generar = driver.find_element(by=By.XPATH, value='//*[@id="SupermercadosBBRecommercemain-1228722670"]/div/div[2]/div/div/div/div/div/div/div[2]/div/div/div[3]/div/div/div/div/div[2]/div/div/div/div/div/div/div[1]/div/div[1]/div/div/div/div[4]/div/div/div')
    boton_generar.click()

def selecionarCeldaTable(driver):
    print('Seleccionar celda')
    element_table = driver.find_elements(by=By.TAG_NAME, value='table')
    table_data = element_table[1]
    element_tbody = table_data.find_element(by=By.TAG_NAME, value='tbody')
    time.sleep(2)

    #obtenemos los valores
    elements_tr_table = element_tbody.find_elements(by=By.TAG_NAME, value='tr')
    print(len(elements_tr_table))

    #sin los 2 ultimos
    elements_tr_table_aux = elements_tr_table[:-2]


    for element in elements_tr_table_aux:
        print("---------- tr -----------")
        elements_td_from_tr = element.find_elements(by=By.TAG_NAME, value='td')
        count = 0
        for element_td in elements_td_from_tr:
            print(element_td.text)

            if(count == 5 and element_td.text != ""):
                time.sleep(1)
                element_button = element_td.find_element(by=By.CLASS_NAME, value='v-button')
                time.sleep(2)
                element_button.click()
                time.sleep(2)

                #obtenemos la data de la tabla
                elements_table = driver.find_elements(by=By.TAG_NAME, value='table')
                table_data_dialog = elements_table[2]
                table_data_dialog_body = table_data_dialog.find_element(by=By.TAG_NAME, value='tbody')
                table_data_dialog_tr = table_data_dialog_body.find_elements(by=By.TAG_NAME, value='tr')
                for element_tr_dialog in table_data_dialog_tr:
                    elements_td_from_tr_dialog = element_tr_dialog.find_elements(by=By.TAG_NAME, value='td')
                    print('-', end=' ')
                    for element_td_dialog in elements_td_from_tr_dialog:
                        print(element_td_dialog.text, end=', ')
                    print()


                boton_close_dialog = driver.find_element(by=By.CLASS_NAME, value='v-window-closebox')
                boton_close_dialog.click()

            count = count + 1

        # hacemos click a la primera celda
        elements_td_from_tr[0].click()

        print("---------- tr -----------")

    # nos desplazamos en la tabla
    actions = ActionChains(driver)
    for _ in range(18):
        actions.send_keys(Keys.ARROW_DOWN)
    actions.perform()


def obtenerDataPorCelda(driver):
    print('obtener data')



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    chrome_options = Options()
    #chrome_options.add_argument("--headless")
    service = Service(executable_path=r'C:\Users\Usuario\PycharmProjects\supermercados-scrap\driver\chromedriver-win64\chromedriver.exe')
    driver = webdriver.Chrome(service=service, options=chrome_options)
    driver.get("https://b2b.intercorpretail.pe/")
    driver.set_window_size(1680, 1050)

    #seleccionar supermercado
    seleccionarSupermercado(driver)
    time.sleep(1)

    #logearse
    loginUsuario(driver)
    time.sleep(3)

    #seleccionar menu
    seleccionarMenu(driver)
    time.sleep(3)

    #generar reporte
    generarInforme(driver)
    time.sleep(3)

    #seleccionar celda
    selecionarCeldaTable(driver)
    time.sleep(60)


    # Cerrar el navegador
    driver.quit()