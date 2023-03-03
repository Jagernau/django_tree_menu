
style = """ 
<style>
/* Кнопка выпадающего списка */
.dropbtn {
  background-color: #4CAF50;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}
.dropbtn-active {
  background-color: #3e8e41;
  color: white;
  padding: 16px;
  font-size: 16px;
  border: none;
}
/* Контейнер <div> - необходим для размещения выпадающего содержимого */
.dropdown {
  position: relative;
  display: block;
}

/* Выпадающее содержимое (скрыто по умолчанию) */
.dropdown-content {
  display: none;
  position: absolute;
  background-color: #f1f1f1;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}
/* Активное Выпад.меню */
.dropdown-content-active {
  display: inline;
  background-color: #3e8e41
  position: absolute;
  min-width: 160px;
  box-shadow: 0px 8px 16px 0px rgba(0,0,0,0.2);
  z-index: 1;
}

/* Ссылки внутри выпадающего списка */
.dropdown-content a {
  color: black;
  padding: 12px 16px;
  text-decoration: none;
  display: inline;
}
/* Изменение цвета выпадающих ссылок при наведении курсора */
.dropdown-content a:hover {background-color: #ddd;}
/* Показать выпадающее меню при наведении курсора */
.dropdown:hover .dropdown-content {display: inline;}

/* Изменение цвета фона кнопки раскрывающегося списка при отображении содержимого раскрывающегося списка */
.dropdown:hover .dropbtn {background-color: #3e8e41;}
</style>

"""

