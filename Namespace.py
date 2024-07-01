def test_function():
    def inner_function():
        print("Я ы области видимости функции test_function")
    inner_function()

# inner_function() функцию вызвать вне test_function() не возможно, так как она находится в локальной области видимости
test_function()