from callLimit import callLimit

@callLimit(3)
def f():
    print("f()")

@callLimit(1)
def g():
    print("g()")

for i in range(3):
    f()
    g()

# Additional edge-case tests
@callLimit(0)
def never():
    print("Should not print")

never()
never()

@callLimit(2)
def with_args(x):
    print(f"with_args: {x}")

with_args(1)
with_args(2)
with_args(3)

# Test that decorator does not affect other functions
def plain():
    print("plain function")

plain()
plain()
