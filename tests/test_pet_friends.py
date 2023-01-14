from api import PetFriends
from settings import valid_email, valid_password
import os

pf = PetFriends()

# Тест 1. Тест на использование неверного пароля 

def test_get_api_key_for_wrong_password(email=valid_email, password=wrong_password):
    """ Проверяем что запрос api ключа возвращает статус 403 при неверном пароле"""

    status, result = pf.get_api_key(email, password)
    assert status == 403

# Тест 2. Некорректный емайл

def test_get_api_key_for_wrong_user(email=wrong_email, password=valid_password):
    """ Проверяем что запрос api ключа возвращает статус 403 в результате использования некорректного емайла"""
   
    status, result = pf.get_api_key(email, password)
    assert status == 403

# Тест 3. Дбоваление нового питомца без фото
def test_add_new_pet_without_photo_valid_data(name='Арсель', animal_type='змея',
                                     age='2'):
    """Проверяем что можно добавить питомца с корректными данными без фото"""

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца без фото
    status, result = pf.add_new_pet_without_photo(auth_key, name, animal_type, age)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 200
    assert result['name'] == name

# Тест 4. Успешное добавление фото
def test_successful_add_photo(pet_photo='imagws/cat1.jpg'):
    """Проверяем возможность добавления фото"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    if len(my_pets['pets']) > 0:
        status, result = pf.add_pet_photo(auth_key, my_pets['pets'][0]['id'], pet_photo)

        assert status == 200
        
# Тест 5. Возвращение списка питомцев пользователя
def test_get_all_pets_with_valid_key(filter='my_pets'):
    """ Проверяем что запрос питомцев пользователя возвращает не пустой список."""
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    status, result = pf.get_list_of_pets(auth_key, filter)

    assert status == 200
    assert len(result['pets']) > 0
    
# Тест 6. Неверный формат данных при обновлении карточки питомца
def test_failed_update_self_pet_info(name='Ливер', animal_type='Попугай', age='пять'):
    """Проверяем невозможность обновления информации о питомце при некорретном формате возраста"""

    # Получаем ключ auth_key и список своих питомцев
    _, auth_key = pf.get_api_key(valid_email, valid_password)
    _, my_pets = pf.get_list_of_pets(auth_key, "my_pets")

    # Если список не пустой, то пробуем обновить его имя, тип и возраст при некорректных данных
    if len(my_pets['pets']) > 0:
        status, result = pf.update_pet_info(auth_key, my_pets['pets'][0]['id'], name, animal_type, age)

        # Проверяем что статус ответа = 400 и такой формат возраста использовать нельзя
        assert status == 400
  
# Тест 7. Некорректный формат изображения

def test_add_new_pet_with_failed_data(name="2", animal_type='123',
                                     age='5', pet_photo='imagws/test.txt'):
    """Проверяем что нельзя добавить питомца с некорректными данными"""

    # Получаем полный путь изображения питомца и сохраняем в переменную pet_photo
    pet_photo = os.path.join(os.path.dirname(__file__), pet_photo)

    # Запрашиваем ключ api и сохраняем в переменую auth_key
    _, auth_key = pf.get_api_key(valid_email, valid_password)

    # Добавляем питомца
    status, result = pf.add_new_pet(auth_key, name, animal_type, age, pet_photo)

    # Сверяем полученный ответ с ожидаемым результатом
    assert status == 400
    assert result['name'] == name

# Тест 8. Некорректный емайл

# Тест 9. Некорректный емайл

# Тест 10. Некорректный емайл

