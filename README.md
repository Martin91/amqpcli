```
┌─┐┌┬┐┌─┐ ┌─┐┌─┐┬  ┬
├─┤││││─┼┐├─┘│  │  │
┴ ┴┴ ┴└─┘└┴  └─┘┴─┘┴
```

An interactive shell developed by Python to be used as a client to communicate with an AMQP broker(server).

It is inspired by [Celery's amqp command line](https://github.com/celery/celery/blob/master/celery/bin/amqp.py), but amqpcli meant to provide a light-weight tool and others can use it without the necessity to install the whole Celery package.   

### Getting Started
1. Install it by pip:
    ```sh
    pip install amqpcli
    ```
    
2. Run the command line:
    ```sh
    amqpcli -H localhost:5672 -u guest -p guest -V /
    ```
    
    That is it!  
    Just try to enter a `help` command to check all available commands and their corresponding usages.
    
Certainly you can also download the source code and run:
```sh
PYTHONPATH=./ bin/amqpcli -H localhost:5672 -u guest -p guest -V /
```