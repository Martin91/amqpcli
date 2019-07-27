amqpcli
====

An interactive shell developed by Python to be used as a client to communicate with an AMQP broker(server).

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