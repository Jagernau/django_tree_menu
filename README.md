# Django Tree Menu App

This is a Django app that implements a tree-like menu that meets the following conditions:

- The menu is implemented via a template tag.
- Everything above the highlighted item is expanded. The first nesting level below the highlighted item is also expanded.
- The menu is stored in the database.
- The menu is editable in the standard Django admin.
- The active menu item is determined based on the URL of the current page.
- There can be several menus on one page. They are determined by the name.
- When you click on a menu, the menu navigates to the specified URL. The URL can be specified either explicitly or through named URL.
- It takes exactly one query to the database to draw each menu.

## Installation

1. Clone the repository to your local machine: `git clone https://github.com/Jagernau/django_tree_menu`
2. Install the app's dependencies: `pip install -r requirements.txt`
3. Migrate the database: `python manage.py migrate`
4. Start the development server: `python manage.py runserver`

## Usage

### Creating menus

1. Log in to the Django admin.
2. Click on the "Menus" link.
3. Click on the "Add menu" button.
4. Enter a name for the menu.
5. Click "Save".

### Adding menu items

1. Click on the menu you want to add items to.
2. Click on the "Add menu item" button.
3. Enter a name for the menu item.
4. Enter the URL for the menu item.
5. Click "Save".

### Drawing menus in templates

To draw a menu in a template, use the following code: `{% draw_menu 'menu_name' %}`

Replace "menu_name" with the name of the menu you want to draw.

## Contributing

If you want to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a new branch with your changes.
3. Make your changes and commit them.
4. Push your changes to your fork.
5. Submit a pull request.



