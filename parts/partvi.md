# Part VI Creating a hot reloadable app client
In this chapter we will develop an app which we can use to test other apps without recompiling them.
As you might have seen building an Android app is a long lasting process.
First you have to find out which standard libraries your app is using, then you have to collect and compile all shared objects for the target platform. This includes Python itself. Then you have to package all of these into an apk and last but not least you have to copy the apk to your device.
On my machine this takes about 5 minutes each time I want to test a change on my device.
Of course you can test a desktop version, but...

The fact that your app has got a Python interpreter included makes it easy to hot reload changes in milliseconds.

So we are writing our *. py and *. qml files, starting a SimpleHttpServer on the development machine and start this special client app on our Android device. This client now loads all changed files via http from the web server and executes them. Isn't that simple?!

Therefore we need a very small app, but with almost all standard libraries included. Maybe one of your apps is going to include them sometime. 

The app itself uses the lib httpimport to load Python files over the internet and imports them as they were stored locally. Also Qt is able to load QML files over the internet. You just have to change the url from local to external.

To begin with here is small sample which you can try on your desktop first.
```python
import httpimport
```