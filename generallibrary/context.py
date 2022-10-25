import sys
from functools import partial
from io import StringIO
from generallibrary.functions import AutoInitBases


class DecoContext(metaclass=AutoInitBases):
    """ A base class which is both contextmanager and decorator.
        Just define before and after.
        Optionally define dunder init, put 'func' as first arg if method should be decoratable without call.
        Works with func being first parameter and without func parameter at all. """
    def __init__(self, func=None):
        self.func = func

    def before(self, *args, **kwargs):
        ...

    def after(self, *args, **kwargs):
        ...

    def __get__(self, instance, owner):
        return partial(self.__call__, instance)

    def __call__(self, *args, **kwargs):
        # print(self, args, kwargs)
        if self.func is None and args and callable(args[0]):
            self.func = args[0]
            return self

        assert self.func, f"{type(self).__name__}.__init__ needs 'func' as first arg for decorating method without call."

        self.before()
        try:
            result = self.func(*args, **kwargs)
        finally:
            self.after()
        return result

    def __enter__(self):
        return self.before()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.after()


class RedirectStdout(DecoContext):
    """ Redirect stdout to None, list, or callable which is given list of strings when called.

        with RedirectStdout(lambda x: Path("foo").write(x, overwrite=True)):
            print("bar")

        l = []
        with RedirectStdout(l):
            print("bar")

        @RedirectStdout
        def x():
            print("bar")
        """
    def __init__(self, *targets):
        self.targets = targets

        self.stringIO_stdout = None

        self.original_stdout = sys.stdout

    def _get_output(self):
        """ :rtype: list[str] """
        return self.stringIO_stdout.getvalue().splitlines()

    def _send_to_target(self, target):
        output = self._get_output()
        if type(target) is list:
            target.extend(output)
        elif callable(target):
            target(output)

    def before(self):
        sys.stdout = self.stringIO_stdout = StringIO()

    def after(self):
        sys.stdout = self.original_stdout

        for target in self.targets:
            self._send_to_target(target=target)



