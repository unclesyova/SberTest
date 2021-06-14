class NewBuilding():
    """Класс, содержащий информацию о новостройке.

    В классе реализован конструктор и метод, возвращающий
    информацию об экземпляре в виде словаря.
    """
    def __init__(self, address, status, appartments_num, builder, 
             land_num, app_sold, square_m_price):
        self.address = address
        self.status = status
        self.appartments_num = appartments_num
        self.builder = builder
        self.land_num = land_num
        self.app_sold = app_sold
        self.square_m_price = square_m_price


    def to_dict(self):
        return {'Адрес': self.address, 
                'Статус': self.status, 
                'Кол-во квартир': self.appartments_num, 
                'Застройщик': self.builder, 
                'Кадастровый номер': self.land_num, 
                'Распроданность': self.app_sold, 
                'Цена(м2)': self.square_m_price}
