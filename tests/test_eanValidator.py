from EanValidator.EanValidator import EanValidator


def test_eanvalidator_returnstrue():
    ean_validator = EanValidator()
    assert ean_validator.validate("4003301018398") == True


def test_eanvalidator_returnsFalse():
    ean_validator = EanValidator()
    assert ean_validator.validate("4003301018392") == False


# testea detalle de implementación
def test_calculateeanalgorithm_returnvalidsum():
    ean_validator = EanValidator()
    sum = ean_validator.calculate_ean_algorithm("400330101839")
    assert sum == 72


# testea detalle de implementación
def test_calculatechecksum_returnvalidchecksum():
    ean_validator = EanValidator()
    sum = ean_validator.calculate_ean_algorithm("400330101839")
    check_sum = ean_validator.calculate_checksum(sum)
    assert check_sum == 8
