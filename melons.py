"""This file should have our order classes in it."""

class AbstractMelonOrder(object):
    """Any melon order placed with UberMelon."""

    def __init__(self, species, qty, country_code):
        """Initialize melon order attributes"""
        self.species = species
        self.qty = qty
        self.shipped = False
        self.country_code = country_code

    def get_total(self):
        """Calculate price."""
        base_price = 5

        if self.species.lower() == "christmas":
            base_price = base_price * 1.5
        
        total = (1 + self.tax) * self.qty * base_price
        return round(total,2)

    def mark_shipped(self):
        """Set shipped to true."""

        self.shipped = True




class DomesticMelonOrder(AbstractMelonOrder):
    """A domestic (in the US) melon order."""
    
    # order_type = "domestic"
    tax = 0.08


    def __init__(self, species, qty):
        """Initialize melon order with attributes"""

        super(DomesticMelonOrder, self).__init__(species, qty, "USA")


    


class InternationalMelonOrder(AbstractMelonOrder):
    """An international (non-US) melon order."""
    # order_type = "international"
    tax = 0.17
    
    def get_total(self):
        """Add $3 to total if order contains less than 10 melons."""
        total = super(InternationalMelonOrder, self).get_total()
        if self.qty < 10:
            return round(total + 3,2)
        else:
            return round(total,2)


    def get_country_code(self):
        """Return the country code."""

        return self.country_code
