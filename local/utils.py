try:
    len(5)
except TypeError:
    print("not supprted")

x = 5


def exceptions_example_1(x):
    try:
        result = len(x)
    except TypeError:
        print(f"Type ({type(x).__name__}) not supported")
    except  ValueError:
        print(f"Value {x} must be [0,100]")
    except Exception as e:
        print(f"Exception {e}")
    else:
        return result
    finally:
        print("Execution completed")

def exceptions_example_2(x: str):
    try:
        result = int(x)
    except  ValueError:
        print(f"Value '{x}'a must be numeric [0,100]")
    except Exception as e:
        print(f"Exception {e}")
    else:
        return result
    finally:
        print("Execution completed")


exceptions_example_2("ar")