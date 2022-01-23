
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verify criticality is balanced.

    :param temperature: temperature value (integer or float)
    :param neutrons_emitted: number of neutrons emitted per second (integer or float)
    :return:  boolean True if conditions met, False if not

    A reactor is said to be critical if it satisfies the following conditions:
    - The temperature is less than 800.
    - The number of neutrons emitted per second is greater than 500.
    - The product of temperature and neutrons emitted per second is less than 500000.
    """
    product_temp_neut = int(temperature) * int(neutrons_emitted)
    if temperature < 800 and neutrons_emitted > 500:
        if product_temp_neut < 500000:
            return(True)
        else: 
            return(False)
    else: 
        return(False)

print(is_criticality_balanced(750, 400))