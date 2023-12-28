"""
The Factory Pattern
    Use cases:
    If you realize that you cannot track the objects created by your application because the code
    that creates them is in many different places instead of in a single function/method, you
    should consider using the factory method pattern. The factory method centralizes object
    creation and tracking your objects becomes much easier. Note that it is absolutely fine to
    create more than one factory method, and this is how it is typically done in practice. Each
    factory method logically groups the creation of objects that have similarities. For example,
    one factory method might be responsible for connecting you to different databases
    (MySQL, SQLite), another factory method might be responsible for creating the geometrical
    object that you request (circle, triangle), and so on.

    The factory method is also useful when you want to decouple object creation from object
    usage. We are not coupled/bound to a specific class when creating an object; we just
    provide partial information about what we want by calling a function. This means that
    introducing changes to the function is easy and does not require any changes to the code
    that uses it.
"""
impo