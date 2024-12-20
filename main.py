from collections import namedtuple

class Product(namedtuple('Product', ['name', 'price', 'quantity'])):
    def total_price(self):
        """
        this method calculates the total price of the product
        :return:
        """
        return self.price * self.quantity

    def is_available(self):
        """
        this method checks if the product is available
        :return:
        """
        return self.quantity > 0

    def apply_discount(self, discount):
        """
        this method applies the discount to the product
        :param discount:
        :return:
        """
        return self.price * (1 - discount / 100)

    def sell(self, amount):
        """
        this method sells the product
        :param amount:
        :return:
        """
        if amount > self.quantity:
            return f"Not enough {self.name} in stock."
        new_quantity = self.quantity - amount
        return Product(self.name, self.price, new_quantity)


class User(namedtuple('User', ['username', 'email', 'age'])):
    def is_adult(self):
        return self.age >= 18

    def contact_info(self):
        """
        this method returns the contact information of the user
        :return:
        """
        return f"Contact {self.username} via {self.email}"

    def update_profile(self, **kwargs):
        """
        this method updates the user's profile information'
        :param kwargs:
        :return:
        """
        data = self._asdict()
        data.update(kwargs)
        return User(**data)

    def welcome_message(self):
        """
        this method returns the welcome message of the user
        :return:
        """
        if self.age < 18:
            return f"Welcome, {self.username}! You're still young and adventurous!"
        return f"Welcome, {self.username}! Enjoy your adult privileges."

product = Product(name='TV', price=1500, quantity=10)
print(f"Total price for {product.name}: ${product.total_price()}")
print(f"Is {product.name} available? {product.is_available()}")
print(f"Price after 10% discount: ${product.apply_discount(10)}")
print(product.sell(3))
print(product.sell(8))

user = User(username='ali_k', email='ali@gmail.com', age=20)
print(f"Is {user.username} an adult? {user.is_adult()}")
print(user.contact_info())
updated_user = user.update_profile(email='ali_new@gmail.com')
print(updated_user.contact_info())
print(user.welcome_message())