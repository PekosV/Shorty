# What is Shorty?

Shorty is a microservice that receives URL and transforms them to short and prettier urls. Shorty supports two providers:
[Bitly](https://www.bitly.com) and [TinyUrl](https://tinyurl.com). So Shorty actually send a request to these providers which handle the shortening
for us. You can either choose one of these providers or otherwise Shorty will use Bitly as the default provider.


# How to use Shorty:
You can run the bash script for running the app.  
Just type:  
```./run.sh```

# How to run the tests:
Type:  
```py.test```

# Request a shortened url

In order for Shorty to shorten your url you should send a request like the example below.  
Note that the provider is optional because Shorty uses Bitly as the default provider in case no provider is requested.  
  
| param    | type   | required | description                        |
|----------|--------|----------|------------------------------------|
| url      | string | Y        | The URL to shorten                 |
| provider | string | N        | The provider to use for shortening |

```{'url': 'https://www.withplum.com', 'provider': 'tinyurl' }```  
or  
```{'url': 'https://www.withplum.com'}```  
# Response from shorty

A valid response from shorty should look like the following example:  
```
{
    "data": {
        "short_link": "https://bit.ly/3G42h5P",
        "url": "https://www.withplum.com"
    }
}
```  
or  

```
{
    "data": {
        "short_link": "https://tinyurl.com/2bn863up",
        "url": "https://www.withplum.com"
    }
}
```

# How Shorty was build:

When Shorty receives a request firstly it verifies the user input. We verify that the URL is valid and that the requested provider
is a valid option. For the URL verification I used the validators package.After the verification is done we continue to send the url
to the requested provider. If by any chance the server is unavailable (i check for status code 503) we return a message that
prompts the user to try a different provider. If something goes wrong during execution (e.g. the user requested an invalid url)
we raise the appropriate exception and send back a message explaining what went wrong.


# What could have been better

In my opinion there is plenty room for improvement in my implementation of Shorty.  
For example the use of Docker could have been great as the project could have been more portable and lightweight.  
Another improvement is to write code to mock the provider's behaviour. That would make testing less dependable to third party
services.

# What was used to build Shorty
- Flask (https://flask.palletsprojects.com/en/2.0.x/)
- Pytest (https://docs.pytest.org/en/6.2.x/)
- Providers (https://validators.readthedocs.io/en/latest/)
- Requests (https://docs.python-requests.org/en/latest/)
