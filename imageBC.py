Last login: Tue Jun 25 18:06:38 on ttys001
-bash: /Users/shoichi/.bash_profile: line 1: syntax error near unexpected token `then'
-bash: /Users/shoichi/.bash_profile: line 1: `if[ -f ~/.bashrc ]; then'
YaCnoMacBook-puro:~ shoichi$ python -m venv test
/usr/local/opt/python@2/bin/python2.7: No module named venv
YaCnoMacBook-puro:~ shoichi$ python3 -m venv test
YaCnoMacBook-puro:~ shoichi$ source test/bin/activate
(test) YaCnoMacBook-puro:~ shoichi$ pip install keras
Collecting keras
  Using cached https://files.pythonhosted.org/packages/5e/10/aa32dad071ce52b5502266b5c659451cfd6ffcbf14e6c8c4f16c0ff5aaab/Keras-2.2.4-py2.py3-none-any.whl
Collecting six>=1.9.0 (from keras)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Collecting h5py (from keras)
  Using cached https://files.pythonhosted.org/packages/80/c5/eec74d7324628f1b640c6e706981c4ed51afcaa1656ece26cb08d862598e/h5py-2.9.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting scipy>=0.14 (from keras)
  Using cached https://files.pythonhosted.org/packages/04/66/ec5f1283d6a290a9153881a896837487338c44639c1305cc59e1c7b69cc9/scipy-1.3.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting keras-applications>=1.0.6 (from keras)
  Using cached https://files.pythonhosted.org/packages/71/e3/19762fdfc62877ae9102edf6342d71b28fbfd9dea3d2f96a882ce099b03f/Keras_Applications-1.0.8-py3-none-any.whl
Collecting pyyaml (from keras)
  Using cached https://files.pythonhosted.org/packages/a3/65/837fefac7475963d1eccf4aa684c23b95aa6c1d033a2c5965ccb11e22623/PyYAML-5.1.1.tar.gz
Collecting numpy>=1.9.1 (from keras)
  Using cached https://files.pythonhosted.org/packages/6b/be/608b7f72b851472388eafc010a5d46dae5d41610d0ac5df4c98c2ed1b865/numpy-1.16.4-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting keras-preprocessing>=1.0.5 (from keras)
  Using cached https://files.pythonhosted.org/packages/28/6a/8c1f62c37212d9fc441a7e26736df51ce6f0e38455816445471f10da4f0a/Keras_Preprocessing-1.1.0-py2.py3-none-any.whl
Installing collected packages: six, numpy, h5py, scipy, keras-applications, pyyaml, keras-preprocessing, keras
  Running setup.py install for pyyaml ... done
Successfully installed h5py-2.9.0 keras-2.2.4 keras-applications-1.0.8 keras-preprocessing-1.1.0 numpy-1.16.4 pyyaml-5.1.1 scipy-1.3.0 six-1.12.0
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:~ shoichi$ pip install sklearn,tensorflow
Invalid requirement: 'sklearn,tensorflow'
Traceback (most recent call last):
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/packaging/requirements.py", line 93, in __init__
    req = REQUIREMENT.parseString(requirement_string)
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1654, in parseString
    raise exc
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1644, in parseString
    loc, tokens = self._parse( instring, 0 )
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1402, in _parseNoCache
    loc,tokens = self.parseImpl( instring, preloc, doActions )
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 3417, in parseImpl
    loc, exprtokens = e._parse( instring, loc, doActions )
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 1406, in _parseNoCache
    loc,tokens = self.parseImpl( instring, preloc, doActions )
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/pyparsing.py", line 3205, in parseImpl
    raise ParseException(instring, loc, self.errmsg, self)
pip._vendor.pyparsing.ParseException: Expected stringEnd (at char 7), (line:1, col:8)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_internal/req/constructors.py", line 253, in install_req_from_line
    req = Requirement(req)
  File "/Users/shoichi/test/lib/python3.7/site-packages/pip/_vendor/packaging/requirements.py", line 96, in __init__
    requirement_string[e.loc:e.loc + 8], e.msg
pip._vendor.packaging.requirements.InvalidRequirement: Parse error at "',tensorf'": Expected stringEnd

You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:~ shoichi$ pip install sklearn
Collecting sklearn
Collecting scikit-learn (from sklearn)
  Using cached https://files.pythonhosted.org/packages/aa/7d/6c71c35c201f6d5cec318c7ed7841317adbf291513742865ed8904ae4ea9/scikit_learn-0.21.2-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Requirement already satisfied: numpy>=1.11.0 in ./test/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.16.4)
Collecting joblib>=0.11 (from scikit-learn->sklearn)
  Using cached https://files.pythonhosted.org/packages/cd/c1/50a758e8247561e58cb87305b1e90b171b8c767b15b12a1734001f41d356/joblib-0.13.2-py2.py3-none-any.whl
Requirement already satisfied: scipy>=0.17.0 in ./test/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.3.0)
Installing collected packages: joblib, scikit-learn, sklearn
Successfully installed joblib-0.13.2 scikit-learn-0.21.2 sklearn-0.0
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:~ shoichi$ pip install tensorflow
Collecting tensorflow
  Using cached https://files.pythonhosted.org/packages/ed/11/037887c5cbac5af3124050fb6348e67caa038734cc9673b11c31c8939072/tensorflow-1.14.0-cp37-cp37m-macosx_10_11_x86_64.whl
Requirement already satisfied: keras-applications>=1.0.6 in ./test/lib/python3.7/site-packages (from tensorflow) (1.0.8)
Collecting wrapt>=1.11.1 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz
Requirement already satisfied: numpy<2.0,>=1.14.5 in ./test/lib/python3.7/site-packages (from tensorflow) (1.16.4)
Collecting protobuf>=3.6.1 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/fd/ed/e53989e7b08274334ddb41dac51294d270b3db7b3d1e354f5b548714c7c6/protobuf-3.8.0-cp37-cp37m-macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting termcolor>=1.1.0 (from tensorflow)
Collecting gast>=0.2.0 (from tensorflow)
Requirement already satisfied: six>=1.10.0 in ./test/lib/python3.7/site-packages (from tensorflow) (1.12.0)
Collecting grpcio>=1.8.6 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/5e/71/92d142dcc3337dbafb6f1d936b19b94a1f65efc9bc3ddfb2315710068025/grpcio-1.21.1-cp37-cp37m-macosx_10_9_x86_64.whl
Collecting google-pasta>=0.1.6 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/d0/33/376510eb8d6246f3c30545f416b2263eee461e40940c2a4413c711bdf62d/google_pasta-0.1.7-py3-none-any.whl
Requirement already satisfied: keras-preprocessing>=1.0.5 in ./test/lib/python3.7/site-packages (from tensorflow) (1.1.0)
Collecting tensorboard<1.15.0,>=1.14.0 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/91/2d/2ed263449a078cd9c8a9ba50ebd50123adf1f8cfbea1492f9084169b89d9/tensorboard-1.14.0-py3-none-any.whl
Collecting absl-py>=0.7.0 (from tensorflow)
Collecting tensorflow-estimator<1.15.0rc0,>=1.14.0rc0 (from tensorflow)
  Downloading https://files.pythonhosted.org/packages/3c/d5/21860a5b11caf0678fbc8319341b0ae21a07156911132e0e71bffed0510d/tensorflow_estimator-1.14.0-py2.py3-none-any.whl (488kB)
    100% |████████████████████████████████| 491kB 1.2MB/s 
Collecting astor>=0.6.0 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/d1/4f/950dfae467b384fc96bc6469de25d832534f6b4441033c39f914efd13418/astor-0.8.0-py2.py3-none-any.whl
Collecting wheel>=0.26 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/bb/10/44230dd6bf3563b8f227dbf344c908d412ad2ff48066476672f3a72e174e/wheel-0.33.4-py2.py3-none-any.whl
Requirement already satisfied: h5py in ./test/lib/python3.7/site-packages (from keras-applications>=1.0.6->tensorflow) (2.9.0)
Requirement already satisfied: setuptools in ./test/lib/python3.7/site-packages (from protobuf>=3.6.1->tensorflow) (40.6.2)
Collecting werkzeug>=0.11.15 (from tensorboard<1.15.0,>=1.14.0->tensorflow)
  Using cached https://files.pythonhosted.org/packages/9f/57/92a497e38161ce40606c27a86759c6b92dd34fcdb33f64171ec559257c02/Werkzeug-0.15.4-py2.py3-none-any.whl
Collecting markdown>=2.6.8 (from tensorboard<1.15.0,>=1.14.0->tensorflow)
  Using cached https://files.pythonhosted.org/packages/c0/4e/fd492e91abdc2d2fcb70ef453064d980688762079397f779758e055f6575/Markdown-3.1.1-py2.py3-none-any.whl
tensorboard 1.14.0 has requirement setuptools>=41.0.0, but you'll have setuptools 40.6.2 which is incompatible.
Installing collected packages: wrapt, protobuf, termcolor, gast, grpcio, google-pasta, werkzeug, wheel, markdown, absl-py, tensorboard, tensorflow-estimator, astor, tensorflow
  Running setup.py install for wrapt ... done
Successfully installed absl-py-0.7.1 astor-0.8.0 gast-0.2.2 google-pasta-0.1.7 grpcio-1.21.1 markdown-3.1.1 protobuf-3.8.0 tensorboard-1.14.0 tensorflow-1.14.0 tensorflow-estimator-1.14.0 termcolor-1.1.0 werkzeug-0.15.4 wheel-0.33.4 wrapt-1.11.2
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:~ shoichi$ pip list
Package              Version
-------------------- -------
absl-py              0.7.1  
astor                0.8.0  
gast                 0.2.2  
google-pasta         0.1.7  
grpcio               1.21.1 
h5py                 2.9.0  
joblib               0.13.2 
Keras                2.2.4  
Keras-Applications   1.0.8  
Keras-Preprocessing  1.1.0  
Markdown             3.1.1  
numpy                1.16.4 
pip                  18.1   
protobuf             3.8.0  
PyYAML               5.1.1  
scikit-learn         0.21.2 
scipy                1.3.0  
setuptools           40.6.2 
six                  1.12.0 
sklearn              0.0    
tensorboard          1.14.0 
tensorflow           1.14.0 
tensorflow-estimator 1.14.0 
termcolor            1.1.0  
Werkzeug             0.15.4 
wheel                0.33.4 
wrapt                1.11.2 
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:~ shoichi$ cd python
(test) YaCnoMacBook-puro:python shoichi$ ls
zemi.py
(test) YaCnoMacBook-puro:python shoichi$ deactivate
YaCnoMacBook-puro:python shoichi$ cd ../
YaCnoMacBook-puro:~ shoichi$ cd Desktop/
YaCnoMacBook-puro:Desktop shoichi$ cd research_git/
YaCnoMacBook-puro:research_git shoichi$ ls
README.md		cifar-10-batches-py	keras_cifar.py		requirements.txt
cifar			images			local_cifar.py		train1000-master
YaCnoMacBook-puro:research_git shoichi$ cd train1000-master/
YaCnoMacBook-puro:train1000-master shoichi$ ls
README.md		c.png			e.png			sample1.png		sample_cifar100.py	trainwith1000result.txt
WiG			d.png			get_models.sh		sample2.png		sample_mnist.csv	untitled2.py
__pycache__		data.py			my1000sample.py		sample_cifar10.csv	sample_mnist.hdf5	untitled4.py
a.png			demon1.png		myTrainwith1000.py	sample_cifar10.hdf5	sample_mnist.py		wig_ensemble_cifar.py
b.png			demon2.png		sample			sample_cifar10.py	train1000.py		wig_ensemble_mnist.py
YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
YaCnoMacBook-puro:train1000-master shoichi$ python -m venv test
/usr/local/opt/python@2/bin/python2.7: No module named venv
YaCnoMacBook-puro:train1000-master shoichi$ python3 -m venv test
YaCnoMacBook-puro:train1000-master shoichi$ source test/bin/activate
(test) YaCnoMacBook-puro:train1000-master shoichi$ pip install keras
Collecting keras
  Using cached https://files.pythonhosted.org/packages/5e/10/aa32dad071ce52b5502266b5c659451cfd6ffcbf14e6c8c4f16c0ff5aaab/Keras-2.2.4-py2.py3-none-any.whl
Collecting h5py (from keras)
  Using cached https://files.pythonhosted.org/packages/80/c5/eec74d7324628f1b640c6e706981c4ed51afcaa1656ece26cb08d862598e/h5py-2.9.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting numpy>=1.9.1 (from keras)
  Using cached https://files.pythonhosted.org/packages/6b/be/608b7f72b851472388eafc010a5d46dae5d41610d0ac5df4c98c2ed1b865/numpy-1.16.4-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting keras-preprocessing>=1.0.5 (from keras)
  Using cached https://files.pythonhosted.org/packages/28/6a/8c1f62c37212d9fc441a7e26736df51ce6f0e38455816445471f10da4f0a/Keras_Preprocessing-1.1.0-py2.py3-none-any.whl
Collecting scipy>=0.14 (from keras)
  Using cached https://files.pythonhosted.org/packages/04/66/ec5f1283d6a290a9153881a896837487338c44639c1305cc59e1c7b69cc9/scipy-1.3.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting keras-applications>=1.0.6 (from keras)
  Using cached https://files.pythonhosted.org/packages/71/e3/19762fdfc62877ae9102edf6342d71b28fbfd9dea3d2f96a882ce099b03f/Keras_Applications-1.0.8-py3-none-any.whl
Collecting pyyaml (from keras)
  Using cached https://files.pythonhosted.org/packages/a3/65/837fefac7475963d1eccf4aa684c23b95aa6c1d033a2c5965ccb11e22623/PyYAML-5.1.1.tar.gz
Collecting six>=1.9.0 (from keras)
  Using cached https://files.pythonhosted.org/packages/73/fb/00a976f728d0d1fecfe898238ce23f502a721c0ac0ecfedb80e0d88c64e9/six-1.12.0-py2.py3-none-any.whl
Installing collected packages: numpy, six, h5py, keras-preprocessing, scipy, keras-applications, pyyaml, keras
  Running setup.py install for pyyaml ... done
Successfully installed h5py-2.9.0 keras-2.2.4 keras-applications-1.0.8 keras-preprocessing-1.1.0 numpy-1.16.4 pyyaml-5.1.1 scipy-1.3.0 six-1.12.0
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:train1000-master shoichi$ pip install tensorflow
Collecting tensorflow
  Using cached https://files.pythonhosted.org/packages/ed/11/037887c5cbac5af3124050fb6348e67caa038734cc9673b11c31c8939072/tensorflow-1.14.0-cp37-cp37m-macosx_10_11_x86_64.whl
Requirement already satisfied: keras-applications>=1.0.6 in ./test/lib/python3.7/site-packages (from tensorflow) (1.0.8)
Collecting absl-py>=0.7.0 (from tensorflow)
Collecting wrapt>=1.11.1 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/23/84/323c2415280bc4fc880ac5050dddfb3c8062c2552b34c2e512eb4aa68f79/wrapt-1.11.2.tar.gz
Collecting wheel>=0.26 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/bb/10/44230dd6bf3563b8f227dbf344c908d412ad2ff48066476672f3a72e174e/wheel-0.33.4-py2.py3-none-any.whl
Collecting astor>=0.6.0 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/d1/4f/950dfae467b384fc96bc6469de25d832534f6b4441033c39f914efd13418/astor-0.8.0-py2.py3-none-any.whl
Collecting tensorboard<1.15.0,>=1.14.0 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/91/2d/2ed263449a078cd9c8a9ba50ebd50123adf1f8cfbea1492f9084169b89d9/tensorboard-1.14.0-py3-none-any.whl
Requirement already satisfied: numpy<2.0,>=1.14.5 in ./test/lib/python3.7/site-packages (from tensorflow) (1.16.4)
Requirement already satisfied: six>=1.10.0 in ./test/lib/python3.7/site-packages (from tensorflow) (1.12.0)
Collecting gast>=0.2.0 (from tensorflow)
Collecting google-pasta>=0.1.6 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/d0/33/376510eb8d6246f3c30545f416b2263eee461e40940c2a4413c711bdf62d/google_pasta-0.1.7-py3-none-any.whl
Collecting protobuf>=3.6.1 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/fd/ed/e53989e7b08274334ddb41dac51294d270b3db7b3d1e354f5b548714c7c6/protobuf-3.8.0-cp37-cp37m-macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting termcolor>=1.1.0 (from tensorflow)
Collecting grpcio>=1.8.6 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/5e/71/92d142dcc3337dbafb6f1d936b19b94a1f65efc9bc3ddfb2315710068025/grpcio-1.21.1-cp37-cp37m-macosx_10_9_x86_64.whl
Collecting tensorflow-estimator<1.15.0rc0,>=1.14.0rc0 (from tensorflow)
  Using cached https://files.pythonhosted.org/packages/3c/d5/21860a5b11caf0678fbc8319341b0ae21a07156911132e0e71bffed0510d/tensorflow_estimator-1.14.0-py2.py3-none-any.whl
Requirement already satisfied: keras-preprocessing>=1.0.5 in ./test/lib/python3.7/site-packages (from tensorflow) (1.1.0)
Requirement already satisfied: h5py in ./test/lib/python3.7/site-packages (from keras-applications>=1.0.6->tensorflow) (2.9.0)
Collecting markdown>=2.6.8 (from tensorboard<1.15.0,>=1.14.0->tensorflow)
  Using cached https://files.pythonhosted.org/packages/c0/4e/fd492e91abdc2d2fcb70ef453064d980688762079397f779758e055f6575/Markdown-3.1.1-py2.py3-none-any.whl
Collecting setuptools>=41.0.0 (from tensorboard<1.15.0,>=1.14.0->tensorflow)
  Using cached https://files.pythonhosted.org/packages/ec/51/f45cea425fd5cb0b0380f5b0f048ebc1da5b417e48d304838c02d6288a1e/setuptools-41.0.1-py2.py3-none-any.whl
Collecting werkzeug>=0.11.15 (from tensorboard<1.15.0,>=1.14.0->tensorflow)
  Using cached https://files.pythonhosted.org/packages/9f/57/92a497e38161ce40606c27a86759c6b92dd34fcdb33f64171ec559257c02/Werkzeug-0.15.4-py2.py3-none-any.whl
Installing collected packages: absl-py, wrapt, wheel, astor, setuptools, markdown, protobuf, werkzeug, grpcio, tensorboard, gast, google-pasta, termcolor, tensorflow-estimator, tensorflow
  Running setup.py install for wrapt ... done
  Found existing installation: setuptools 40.6.2
    Uninstalling setuptools-40.6.2:
      Successfully uninstalled setuptools-40.6.2
Successfully installed absl-py-0.7.1 astor-0.8.0 gast-0.2.2 google-pasta-0.1.7 grpcio-1.21.1 markdown-3.1.1 protobuf-3.8.0 setuptools-41.0.1 tensorboard-1.14.0 tensorflow-1.14.0 tensorflow-estimator-1.14.0 termcolor-1.1.0 werkzeug-0.15.4 wheel-0.33.4 wrapt-1.11.2
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:train1000-master shoichi$ pip install sklearn
Collecting sklearn
Collecting scikit-learn (from sklearn)
  Using cached https://files.pythonhosted.org/packages/aa/7d/6c71c35c201f6d5cec318c7ed7841317adbf291513742865ed8904ae4ea9/scikit_learn-0.21.2-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Requirement already satisfied: numpy>=1.11.0 in ./test/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.16.4)
Collecting joblib>=0.11 (from scikit-learn->sklearn)
  Using cached https://files.pythonhosted.org/packages/cd/c1/50a758e8247561e58cb87305b1e90b171b8c767b15b12a1734001f41d356/joblib-0.13.2-py2.py3-none-any.whl
Requirement already satisfied: scipy>=0.17.0 in ./test/lib/python3.7/site-packages (from scikit-learn->sklearn) (1.3.0)
Installing collected packages: joblib, scikit-learn, sklearn
Successfully installed joblib-0.13.2 scikit-learn-0.21.2 sklearn-0.0
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:train1000-master shoichi$ ls
README.md		c.png			e.png			sample			sample_cifar10.py	test			wig_ensemble_cifar.py
WiG			d.png			get_models.sh		sample1.png		sample_cifar100.py	train1000.py		wig_ensemble_mnist.py
__pycache__		data.py			imageBC.py		sample2.png		sample_mnist.csv	trainwith1000result.txt
a.png			demon1.png		my1000sample.py		sample_cifar10.csv	sample_mnist.hdf5	untitled2.py
b.png			demon2.png		myTrainwith1000.py	sample_cifar10.hdf5	sample_mnist.py		untitled4.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Traceback (most recent call last):
  File "imageBC.py", line 9, in <module>
    from PIL import Image
ModuleNotFoundError: No module named 'PIL'
(test) YaCnoMacBook-puro:train1000-master shoichi$ pip install pillow
Collecting pillow
  Using cached https://files.pythonhosted.org/packages/22/55/2ce41fa510f131c776112a1d24ee90cddffc96f1bf0311efb14fdd8ae877/Pillow-6.0.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Installing collected packages: pillow
Successfully installed pillow-6.0.0
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Traceback (most recent call last):
  File "imageBC.py", line 11, in <module>
    import cv2
ModuleNotFoundError: No module named 'cv2'
(test) YaCnoMacBook-puro:train1000-master shoichi$ pip install opencv-python
Collecting opencv-python
  Using cached https://files.pythonhosted.org/packages/8d/ff/13e77ee7ac431f831e20d81a6bf0214ca1cf550cf9b575e3213e14325c81/opencv_python-4.1.0.25-cp37-cp37m-macosx_10_7_x86_64.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Requirement already satisfied: numpy>=1.14.5 in ./test/lib/python3.7/site-packages (from opencv-python) (1.16.4)
Installing collected packages: opencv-python
Successfully installed opencv-python-4.1.0.25
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 60
    batch_size = 10
                  ^
TabError: inconsistent use of tabs and spaces in indentation
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 66
    eva=model.evaluate(X_train,Y_train,verbose=1)
                                                ^
IndentationError: unindent does not match any outer indentation level
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 62, in <module>
    model = model()
  File "imageBC.py", line 17, in model
    model = Sequential()
NameError: name 'Sequential' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 15, in <module>
    import matplotlib.pyplot as plt
ModuleNotFoundError: No module named 'matplotlib'
(test) YaCnoMacBook-puro:train1000-master shoichi$ pip install matplotlib
Collecting matplotlib
  Using cached https://files.pythonhosted.org/packages/ea/de/8c82ad7acc647357bc76d6a90385cba7df8e57d99e25ca38e5e12178682f/matplotlib-3.1.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting kiwisolver>=1.0.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/df/93/8bc9b52a8846be2b9572aa0a7c881930939b06e4abe1162da6a0430b794f/kiwisolver-1.1.0-cp37-cp37m-macosx_10_6_intel.macosx_10_9_intel.macosx_10_9_x86_64.macosx_10_10_intel.macosx_10_10_x86_64.whl
Collecting pyparsing!=2.0.4,!=2.1.2,!=2.1.6,>=2.0.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/dd/d9/3ec19e966301a6e25769976999bd7bbe552016f0d32b577dc9d63d2e0c49/pyparsing-2.4.0-py2.py3-none-any.whl
Requirement already satisfied: numpy>=1.11 in ./test/lib/python3.7/site-packages (from matplotlib) (1.16.4)
Collecting cycler>=0.10 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/f7/d2/e07d3ebb2bd7af696440ce7e754c59dd546ffe1bbe732c8ab68b9c834e61/cycler-0.10.0-py2.py3-none-any.whl
Collecting python-dateutil>=2.1 (from matplotlib)
  Using cached https://files.pythonhosted.org/packages/41/17/c62faccbfbd163c7f57f3844689e3a78bae1f403648a6afb1d0866d87fbb/python_dateutil-2.8.0-py2.py3-none-any.whl
Requirement already satisfied: setuptools in ./test/lib/python3.7/site-packages (from kiwisolver>=1.0.1->matplotlib) (41.0.1)
Requirement already satisfied: six in ./test/lib/python3.7/site-packages (from cycler>=0.10->matplotlib) (1.12.0)
Installing collected packages: kiwisolver, pyparsing, cycler, python-dateutil, matplotlib
Successfully installed cycler-0.10.0 kiwisolver-1.1.0 matplotlib-3.1.0 pyparsing-2.4.0 python-dateutil-2.8.0
You are using pip version 18.1, however version 19.1.1 is available.
You should consider upgrading via the 'pip install --upgrade pip' command.
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 16:37:27.591693 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 16:37:27.708120 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 16:37:27.769967 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 16:37:27.836590 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 16:37:27.837933 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 16:37:27.843963 4676380096 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 16:37:27.844156 4676380096 nn_ops.py:4224] Large dropout rate: 0.7 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
W0626 16:37:27.915162 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 16:37:27.920011 4676380096 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 16, 16, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 8192)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               4194816   
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_3 (Activation)    (None, 10)                0         
=================================================================
Total params: 4,200,842
Trainable params: 4,200,842
Non-trainable params: 0
_________________________________________________________________
W0626 16:37:28.067162 4676380096 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/5
2019-06-26 16:37:28.281991: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 4s 5ms/step - loss: 2.2889 - categorical_crossentropy: 2.2889 - acc: 0.1689 - val_loss: 2.0865 - val_categorical_crossentropy: 2.0865 - val_acc: 0.1600
Epoch 2/5
900/900 [==============================] - 3s 4ms/step - loss: 2.0828 - categorical_crossentropy: 2.0828 - acc: 0.2411 - val_loss: 2.1301 - val_categorical_crossentropy: 2.1301 - val_acc: 0.2400
Epoch 3/5
900/900 [==============================] - 3s 4ms/step - loss: 1.9997 - categorical_crossentropy: 1.9997 - acc: 0.2822 - val_loss: 1.9717 - val_categorical_crossentropy: 1.9717 - val_acc: 0.4100
Epoch 4/5
900/900 [==============================] - 4s 5ms/step - loss: 1.9034 - categorical_crossentropy: 1.9034 - acc: 0.3311 - val_loss: 2.1562 - val_categorical_crossentropy: 2.1562 - val_acc: 0.1800
Epoch 5/5
900/900 [==============================] - 3s 4ms/step - loss: 1.7921 - categorical_crossentropy: 1.7921 - acc: 0.3544 - val_loss: 2.2174 - val_categorical_crossentropy: 2.2174 - val_acc: 0.2300
train data:
1000/1000 [==============================] - 0s 182us/step
categorical_crossentropy :  1.7002464408874511

test data:
10000/10000 [==============================] - 2s 168us/step
acc :  0.2142

test data:
10000/10000 [==============================] - 2s 170us/step
categorical_crossentropy :  2.5716091632843017
acc :  0.2142
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 16:38:51.803971 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 16:38:51.821346 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 16:38:51.824109 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 16:38:51.844657 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 16:38:51.846673 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 16:38:51.855392 4449011136 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 16:38:51.855659 4449011136 nn_ops.py:4224] Large dropout rate: 0.7 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
W0626 16:38:51.935224 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 16:38:51.941879 4449011136 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 16, 16, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 8192)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               4194816   
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_3 (Activation)    (None, 10)                0         
=================================================================
Total params: 4,200,842
Trainable params: 4,200,842
Non-trainable params: 0
_________________________________________________________________
W0626 16:38:52.033410 4449011136 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 16:38:52.246193: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 4s 4ms/step - loss: 2.2096 - categorical_crossentropy: 2.2096 - acc: 0.1833 - val_loss: 2.0620 - val_categorical_crossentropy: 2.0620 - val_acc: 0.2600
Epoch 2/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0434 - categorical_crossentropy: 2.0434 - acc: 0.2467 - val_loss: 2.1343 - val_categorical_crossentropy: 2.1343 - val_acc: 0.1800
Epoch 3/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9228 - categorical_crossentropy: 1.9228 - acc: 0.3200 - val_loss: 2.0881 - val_categorical_crossentropy: 2.0881 - val_acc: 0.2300
Epoch 4/30
900/900 [==============================] - 3s 4ms/step - loss: 1.8174 - categorical_crossentropy: 1.8174 - acc: 0.3611 - val_loss: 1.9591 - val_categorical_crossentropy: 1.9591 - val_acc: 0.2500
Epoch 5/30
900/900 [==============================] - 3s 4ms/step - loss: 1.7040 - categorical_crossentropy: 1.7040 - acc: 0.4056 - val_loss: 2.0726 - val_categorical_crossentropy: 2.0726 - val_acc: 0.3600
Epoch 6/30
900/900 [==============================] - 3s 4ms/step - loss: 1.5984 - categorical_crossentropy: 1.5984 - acc: 0.4100 - val_loss: 2.1572 - val_categorical_crossentropy: 2.1572 - val_acc: 0.2900
Epoch 7/30
900/900 [==============================] - 3s 4ms/step - loss: 1.5185 - categorical_crossentropy: 1.5185 - acc: 0.4400 - val_loss: 2.4254 - val_categorical_crossentropy: 2.4254 - val_acc: 0.1700
Epoch 8/30
900/900 [==============================] - 4s 4ms/step - loss: 1.4713 - categorical_crossentropy: 1.4713 - acc: 0.4667 - val_loss: 2.3582 - val_categorical_crossentropy: 2.3582 - val_acc: 0.2800
Epoch 9/30
900/900 [==============================] - 3s 4ms/step - loss: 1.4074 - categorical_crossentropy: 1.4074 - acc: 0.4667 - val_loss: 2.3591 - val_categorical_crossentropy: 2.3591 - val_acc: 0.2800
Epoch 10/30
900/900 [==============================] - 3s 4ms/step - loss: 1.3101 - categorical_crossentropy: 1.3101 - acc: 0.5089 - val_loss: 2.6588 - val_categorical_crossentropy: 2.6588 - val_acc: 0.2400
Epoch 11/30
900/900 [==============================] - 3s 4ms/step - loss: 1.3049 - categorical_crossentropy: 1.3049 - acc: 0.4944 - val_loss: 2.7122 - val_categorical_crossentropy: 2.7122 - val_acc: 0.2400
Epoch 12/30
900/900 [==============================] - 3s 4ms/step - loss: 1.2975 - categorical_crossentropy: 1.2975 - acc: 0.5033 - val_loss: 2.7310 - val_categorical_crossentropy: 2.7310 - val_acc: 0.2800
Epoch 13/30
900/900 [==============================] - 3s 4ms/step - loss: 1.2138 - categorical_crossentropy: 1.2138 - acc: 0.5267 - val_loss: 2.9096 - val_categorical_crossentropy: 2.9096 - val_acc: 0.1600
Epoch 14/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1744 - categorical_crossentropy: 1.1744 - acc: 0.5311 - val_loss: 3.0204 - val_categorical_crossentropy: 3.0204 - val_acc: 0.2100
Epoch 15/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1448 - categorical_crossentropy: 1.1448 - acc: 0.5333 - val_loss: 3.0601 - val_categorical_crossentropy: 3.0601 - val_acc: 0.2000
Epoch 16/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1556 - categorical_crossentropy: 1.1556 - acc: 0.5389 - val_loss: 3.1574 - val_categorical_crossentropy: 3.1574 - val_acc: 0.1300
Epoch 17/30
900/900 [==============================] - 3s 4ms/step - loss: 1.0944 - categorical_crossentropy: 1.0944 - acc: 0.5711 - val_loss: 3.3061 - val_categorical_crossentropy: 3.3061 - val_acc: 0.1700
Epoch 18/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1177 - categorical_crossentropy: 1.1177 - acc: 0.5367 - val_loss: 3.1267 - val_categorical_crossentropy: 3.1267 - val_acc: 0.1500
Epoch 19/30
900/900 [==============================] - 3s 4ms/step - loss: 1.0483 - categorical_crossentropy: 1.0483 - acc: 0.5489 - val_loss: 3.3802 - val_categorical_crossentropy: 3.3802 - val_acc: 0.1500
Epoch 20/30
900/900 [==============================] - 3s 4ms/step - loss: 0.9996 - categorical_crossentropy: 0.9996 - acc: 0.5933 - val_loss: 3.6760 - val_categorical_crossentropy: 3.6760 - val_acc: 0.1300
Epoch 21/30
900/900 [==============================] - 3s 4ms/step - loss: 1.0115 - categorical_crossentropy: 1.0115 - acc: 0.5589 - val_loss: 3.3640 - val_categorical_crossentropy: 3.3640 - val_acc: 0.1100
Epoch 22/30
900/900 [==============================] - 4s 4ms/step - loss: 0.9745 - categorical_crossentropy: 0.9745 - acc: 0.5600 - val_loss: 3.4402 - val_categorical_crossentropy: 3.4402 - val_acc: 0.1300
Epoch 23/30
900/900 [==============================] - 3s 4ms/step - loss: 0.9815 - categorical_crossentropy: 0.9815 - acc: 0.5744 - val_loss: 3.5820 - val_categorical_crossentropy: 3.5820 - val_acc: 0.1500
Epoch 24/30
900/900 [==============================] - 3s 4ms/step - loss: 0.9578 - categorical_crossentropy: 0.9578 - acc: 0.5778 - val_loss: 3.5766 - val_categorical_crossentropy: 3.5766 - val_acc: 0.1700
Epoch 25/30
900/900 [==============================] - 3s 4ms/step - loss: 0.9159 - categorical_crossentropy: 0.9159 - acc: 0.5767 - val_loss: 3.6150 - val_categorical_crossentropy: 3.6150 - val_acc: 0.1700
Epoch 26/30
900/900 [==============================] - 3s 4ms/step - loss: 0.9204 - categorical_crossentropy: 0.9204 - acc: 0.6022 - val_loss: 3.7854 - val_categorical_crossentropy: 3.7854 - val_acc: 0.1700
Epoch 27/30
900/900 [==============================] - 3s 4ms/step - loss: 0.9028 - categorical_crossentropy: 0.9028 - acc: 0.6022 - val_loss: 3.7665 - val_categorical_crossentropy: 3.7665 - val_acc: 0.1700
Epoch 28/30
900/900 [==============================] - 3s 4ms/step - loss: 0.8816 - categorical_crossentropy: 0.8816 - acc: 0.6022 - val_loss: 3.6626 - val_categorical_crossentropy: 3.6626 - val_acc: 0.1300
Epoch 29/30
900/900 [==============================] - 3s 4ms/step - loss: 0.8561 - categorical_crossentropy: 0.8561 - acc: 0.6167 - val_loss: 3.8719 - val_categorical_crossentropy: 3.8719 - val_acc: 0.1300
Epoch 30/30
900/900 [==============================] - 3s 4ms/step - loss: 0.8501 - categorical_crossentropy: 0.8501 - acc: 0.6211 - val_loss: 3.7844 - val_categorical_crossentropy: 3.7844 - val_acc: 0.1600
train data:
1000/1000 [==============================] - 0s 181us/step
categorical_crossentropy :  0.9739989814758301

test data:
10000/10000 [==============================] - 2s 178us/step
acc :  0.2173

test data:
10000/10000 [==============================] - 2s 174us/step
categorical_crossentropy :  2.7517817539215086
acc :  0.2173
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 72, in <module>
    X_train = preprocessing.scale(X_train)
NameError: name 'preprocessing' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 73, in <module>
    X_train = preprocessing.scale(X_train)
NameError: name 'preprocessing' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 74, in <module>
    X_train = preprocessing.scale(X_train)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/sklearn/preprocessing/data.py", line 141, in scale
    force_all_finite='allow-nan')
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/sklearn/utils/validation.py", line 539, in check_array
    % (array.ndim, estimator_name))
ValueError: Found array with dim 4. the scale function expected <= 2.
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 16:51:48.445996 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 16:51:48.563072 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 16:51:48.634461 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 16:51:48.699438 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 16:51:48.700573 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 16:51:48.708283 4578571712 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 16:51:48.708647 4578571712 nn_ops.py:4224] Large dropout rate: 0.7 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
W0626 16:51:48.771625 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 16:51:48.776360 4578571712 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 16, 16, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 8192)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               4194816   
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_3 (Activation)    (None, 10)                0         
=================================================================
Total params: 4,200,842
Trainable params: 4,200,842
Non-trainable params: 0
_________________________________________________________________
Traceback (most recent call last):
  File "imageBC.py", line 80, in <module>
    result = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,verbose=1)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training.py", line 952, in fit
    batch_size=batch_size)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training.py", line 789, in _standardize_user_data
    exception_prefix='target')
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training_utils.py", line 128, in standardize_input_data
    'with shape ' + str(data_shape))
ValueError: Error when checking target: expected activation_3 to have 2 dimensions, but got array with shape (1000, 10, 2)
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 16:52:59.608244 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 16:52:59.621618 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 16:52:59.623642 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 16:52:59.638651 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 16:52:59.639839 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 16:52:59.646363 4474602944 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 16:52:59.646739 4474602944 nn_ops.py:4224] Large dropout rate: 0.7 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
W0626 16:52:59.702906 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 16:52:59.708041 4474602944 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 16, 16, 32)        0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 8192)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               4194816   
_________________________________________________________________
activation_2 (Activation)    (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_3 (Activation)    (None, 10)                0         
=================================================================
Total params: 4,200,842
Trainable params: 4,200,842
Non-trainable params: 0
_________________________________________________________________
W0626 16:52:59.865880 4474602944 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 16:53:00.094717: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 5s 5ms/step - loss: 2.1943 - categorical_crossentropy: 2.1943 - acc: 0.1700 - val_loss: 2.1641 - val_categorical_crossentropy: 2.1641 - val_acc: 0.2100
Epoch 2/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0319 - categorical_crossentropy: 2.0319 - acc: 0.2844 - val_loss: 2.1068 - val_categorical_crossentropy: 2.1068 - val_acc: 0.1800
Epoch 3/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9232 - categorical_crossentropy: 1.9232 - acc: 0.3244 - val_loss: 1.9207 - val_categorical_crossentropy: 1.9207 - val_acc: 0.3900
Epoch 4/30
900/900 [==============================] - 3s 4ms/step - loss: 1.8095 - categorical_crossentropy: 1.8095 - acc: 0.3733 - val_loss: 2.1182 - val_categorical_crossentropy: 2.1182 - val_acc: 0.3200
Epoch 5/30
^CTraceback (most recent call last):
  File "imageBC.py", line 80, in <module>
    result = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,verbose=1)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training.py", line 1039, in fit
    validation_steps=validation_steps)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training_arrays.py", line 199, in fit_loop
    outs = f(ins_batch)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2715, in __call__
    return self._call(inputs)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2675, in _call
    fetched = self._callable_fn(*array_vals)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1458, in __call__
    run_metadata_ptr)
KeyboardInterrupt
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 16:54:31.040055 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 16:54:31.051810 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 16:54:31.057460 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 16:54:31.075769 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:174: The name tf.get_default_session is deprecated. Please use tf.compat.v1.get_default_session instead.

W0626 16:54:31.076030 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:181: The name tf.ConfigProto is deprecated. Please use tf.compat.v1.ConfigProto instead.

2019-06-26 16:54:31.076380: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
W0626 16:54:31.099044 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1834: The name tf.nn.fused_batch_norm is deprecated. Please use tf.compat.v1.nn.fused_batch_norm instead.

W0626 16:54:32.924775 4441208256 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 16:54:32.924976 4441208256 nn_ops.py:4224] Large dropout rate: 0.7 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
W0626 16:54:32.962186 4441208256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 32, 32, 3)         0         
_________________________________________________________________
conv1_pad (ZeroPadding2D)    (None, 33, 33, 3)         0         
_________________________________________________________________
conv1 (Conv2D)               (None, 16, 16, 32)        864       
_________________________________________________________________
conv1_bn (BatchNormalization (None, 16, 16, 32)        128       
_________________________________________________________________
conv1_relu (ReLU)            (None, 16, 16, 32)        0         
_________________________________________________________________
conv_dw_1 (DepthwiseConv2D)  (None, 16, 16, 32)        288       
_________________________________________________________________
conv_dw_1_bn (BatchNormaliza (None, 16, 16, 32)        128       
_________________________________________________________________
conv_dw_1_relu (ReLU)        (None, 16, 16, 32)        0         
_________________________________________________________________
conv_pw_1 (Conv2D)           (None, 16, 16, 64)        2048      
_________________________________________________________________
conv_pw_1_bn (BatchNormaliza (None, 16, 16, 64)        256       
_________________________________________________________________
conv_pw_1_relu (ReLU)        (None, 16, 16, 64)        0         
_________________________________________________________________
conv_pad_2 (ZeroPadding2D)   (None, 17, 17, 64)        0         
_________________________________________________________________
conv_dw_2 (DepthwiseConv2D)  (None, 8, 8, 64)          576       
_________________________________________________________________
conv_dw_2_bn (BatchNormaliza (None, 8, 8, 64)          256       
_________________________________________________________________
conv_dw_2_relu (ReLU)        (None, 8, 8, 64)          0         
_________________________________________________________________
conv_pw_2 (Conv2D)           (None, 8, 8, 128)         8192      
_________________________________________________________________
conv_pw_2_bn (BatchNormaliza (None, 8, 8, 128)         512       
_________________________________________________________________
conv_pw_2_relu (ReLU)        (None, 8, 8, 128)         0         
_________________________________________________________________
conv_dw_3 (DepthwiseConv2D)  (None, 8, 8, 128)         1152      
_________________________________________________________________
conv_dw_3_bn (BatchNormaliza (None, 8, 8, 128)         512       
_________________________________________________________________
conv_dw_3_relu (ReLU)        (None, 8, 8, 128)         0         
_________________________________________________________________
conv_pw_3 (Conv2D)           (None, 8, 8, 128)         16384     
_________________________________________________________________
conv_pw_3_bn (BatchNormaliza (None, 8, 8, 128)         512       
_________________________________________________________________
conv_pw_3_relu (ReLU)        (None, 8, 8, 128)         0         
_________________________________________________________________
conv_pad_4 (ZeroPadding2D)   (None, 9, 9, 128)         0         
_________________________________________________________________
conv_dw_4 (DepthwiseConv2D)  (None, 4, 4, 128)         1152      
_________________________________________________________________
conv_dw_4_bn (BatchNormaliza (None, 4, 4, 128)         512       
_________________________________________________________________
conv_dw_4_relu (ReLU)        (None, 4, 4, 128)         0         
_________________________________________________________________
conv_pw_4 (Conv2D)           (None, 4, 4, 256)         32768     
_________________________________________________________________
conv_pw_4_bn (BatchNormaliza (None, 4, 4, 256)         1024      
_________________________________________________________________
conv_pw_4_relu (ReLU)        (None, 4, 4, 256)         0         
_________________________________________________________________
conv_dw_5 (DepthwiseConv2D)  (None, 4, 4, 256)         2304      
_________________________________________________________________
conv_dw_5_bn (BatchNormaliza (None, 4, 4, 256)         1024      
_________________________________________________________________
conv_dw_5_relu (ReLU)        (None, 4, 4, 256)         0         
_________________________________________________________________
conv_pw_5 (Conv2D)           (None, 4, 4, 256)         65536     
_________________________________________________________________
conv_pw_5_bn (BatchNormaliza (None, 4, 4, 256)         1024      
_________________________________________________________________
conv_pw_5_relu (ReLU)        (None, 4, 4, 256)         0         
_________________________________________________________________
conv_pad_6 (ZeroPadding2D)   (None, 5, 5, 256)         0         
_________________________________________________________________
conv_dw_6 (DepthwiseConv2D)  (None, 2, 2, 256)         2304      
_________________________________________________________________
conv_dw_6_bn (BatchNormaliza (None, 2, 2, 256)         1024      
_________________________________________________________________
conv_dw_6_relu (ReLU)        (None, 2, 2, 256)         0         
_________________________________________________________________
conv_pw_6 (Conv2D)           (None, 2, 2, 512)         131072    
_________________________________________________________________
conv_pw_6_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_6_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_7 (DepthwiseConv2D)  (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_7_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_7_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_7 (Conv2D)           (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_7_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_7_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_8 (DepthwiseConv2D)  (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_8_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_8_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_8 (Conv2D)           (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_8_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_8_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_9 (DepthwiseConv2D)  (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_9_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_9_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_9 (Conv2D)           (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_9_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_9_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_10 (DepthwiseConv2D) (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_10_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_10_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_10 (Conv2D)          (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_10_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_10_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_11 (DepthwiseConv2D) (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_11_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_11_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_11 (Conv2D)          (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_11_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_11_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pad_12 (ZeroPadding2D)  (None, 3, 3, 512)         0         
_________________________________________________________________
conv_dw_12 (DepthwiseConv2D) (None, 1, 1, 512)         4608      
_________________________________________________________________
conv_dw_12_bn (BatchNormaliz (None, 1, 1, 512)         2048      
_________________________________________________________________
conv_dw_12_relu (ReLU)       (None, 1, 1, 512)         0         
_________________________________________________________________
conv_pw_12 (Conv2D)          (None, 1, 1, 1024)        524288    
_________________________________________________________________
conv_pw_12_bn (BatchNormaliz (None, 1, 1, 1024)        4096      
_________________________________________________________________
conv_pw_12_relu (ReLU)       (None, 1, 1, 1024)        0         
_________________________________________________________________
conv_dw_13 (DepthwiseConv2D) (None, 1, 1, 1024)        9216      
_________________________________________________________________
conv_dw_13_bn (BatchNormaliz (None, 1, 1, 1024)        4096      
_________________________________________________________________
conv_dw_13_relu (ReLU)       (None, 1, 1, 1024)        0         
_________________________________________________________________
conv_pw_13 (Conv2D)          (None, 1, 1, 1024)        1048576   
_________________________________________________________________
conv_pw_13_bn (BatchNormaliz (None, 1, 1, 1024)        4096      
_________________________________________________________________
conv_pw_13_relu (ReLU)       (None, 1, 1, 1024)        0         
_________________________________________________________________
global_average_pooling2d_1 ( (None, 1024)              0         
_________________________________________________________________
reshape_1 (Reshape)          (None, 1, 1, 1024)        0         
_________________________________________________________________
dropout (Dropout)            (None, 1, 1, 1024)        0         
_________________________________________________________________
conv_preds (Conv2D)          (None, 1, 1, 10)          10250     
_________________________________________________________________
reshape_2 (Reshape)          (None, 10)                0         
_________________________________________________________________
act_softmax (Activation)     (None, 10)                0         
=================================================================
Total params: 3,239,114
Trainable params: 3,217,226
Non-trainable params: 21,888
_________________________________________________________________
W0626 16:54:33.082655 4441208256 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/30
900/900 [==============================] - 15s 16ms/step - loss: 3.3316 - categorical_crossentropy: 3.3317 - acc: 0.1367 - val_loss: 5.3226 - val_categorical_crossentropy: 5.3226 - val_acc: 0.1300
Epoch 2/30
900/900 [==============================] - 10s 11ms/step - loss: 3.0007 - categorical_crossentropy: 3.0007 - acc: 0.1600 - val_loss: 3.2928 - val_categorical_crossentropy: 3.2928 - val_acc: 0.1400
Epoch 3/30
900/900 [==============================] - 9s 10ms/step - loss: 2.7008 - categorical_crossentropy: 2.7008 - acc: 0.1744 - val_loss: 2.9859 - val_categorical_crossentropy: 2.9859 - val_acc: 0.1100
Epoch 4/30
900/900 [==============================] - 9s 10ms/step - loss: 2.6659 - categorical_crossentropy: 2.6659 - acc: 0.2189 - val_loss: 2.6149 - val_categorical_crossentropy: 2.6149 - val_acc: 0.0700
Epoch 5/30
900/900 [==============================] - 9s 10ms/step - loss: 2.5201 - categorical_crossentropy: 2.5201 - acc: 0.2400 - val_loss: 2.3654 - val_categorical_crossentropy: 2.3654 - val_acc: 0.2300
Epoch 6/30
900/900 [==============================] - 9s 10ms/step - loss: 2.4845 - categorical_crossentropy: 2.4845 - acc: 0.2589 - val_loss: 2.2000 - val_categorical_crossentropy: 2.2000 - val_acc: 0.2400
Epoch 7/30
900/900 [==============================] - 9s 10ms/step - loss: 2.4566 - categorical_crossentropy: 2.4566 - acc: 0.2422 - val_loss: 2.1329 - val_categorical_crossentropy: 2.1329 - val_acc: 0.2200
Epoch 8/30
900/900 [==============================] - 9s 10ms/step - loss: 2.3481 - categorical_crossentropy: 2.3481 - acc: 0.2644 - val_loss: 2.2828 - val_categorical_crossentropy: 2.2828 - val_acc: 0.1600
Epoch 9/30
900/900 [==============================] - 9s 10ms/step - loss: 2.4095 - categorical_crossentropy: 2.4095 - acc: 0.2533 - val_loss: 2.7943 - val_categorical_crossentropy: 2.7944 - val_acc: 0.0800
Epoch 10/30
900/900 [==============================] - 9s 10ms/step - loss: 2.4218 - categorical_crossentropy: 2.4218 - acc: 0.2656 - val_loss: 2.6000 - val_categorical_crossentropy: 2.6000 - val_acc: 0.1500
Epoch 11/30
280/900 [========>.....................] - ETA: 6s - loss: 2.2900 - categorical_crossentropy: 2.2900 - acc: 0.2929^CTraceback (most recent call last):
  File "imageBC.py", line 80, in <module>
    result = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,verbose=1)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training.py", line 1039, in fit
    validation_steps=validation_steps)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training_arrays.py", line 199, in fit_loop
    outs = f(ins_batch)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2715, in __call__
    return self._call(inputs)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2675, in _call
    fetched = self._callable_fn(*array_vals)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1458, in __call__
    run_metadata_ptr)
KeyboardInterrupt
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 78, in <module>
    X_train = Lambda(lambda X_train: tf.image.resize_images(X_train, (224, 224)))(inputs)
NameError: name 'Lambda' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 78, in <module>
    X_train = tf.image.resize_images(X_train, (224, 224))(inputs)
NameError: name 'tf' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:03:57.965354 4431279552 deprecation_wrapper.py:119] From imageBC.py:79: The name tf.image.resize_images is deprecated. Please use tf.image.resize instead.

Traceback (most recent call last):
  File "imageBC.py", line 79, in <module>
    X_train = tf.image.resize_images(X_train, (224, 224))(inputs)
NameError: name 'inputs' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 31
    model.add(Activation('relu'))
                                ^
TabError: inconsistent use of tabs and spaces in indentation
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 51
    model.summary()
                  ^
IndentationError: unindent does not match any outer indentation level
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:08:28.148448 4749837760 deprecation_wrapper.py:119] From imageBC.py:89: The name tf.image.resize_images is deprecated. Please use tf.image.resize instead.

Traceback (most recent call last):
  File "imageBC.py", line 89, in <module>
    X_train = tf.image.resize_images(X_train, (224, 224))(inputs)
NameError: name 'inputs' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 89, in <module>
    model = model()
  File "imageBC.py", line 30, in model
    model.add(Conv2D(32, (3, 3), padding='same',input_shape=X_train.shape[1:]))
AttributeError: 'function' object has no attribute 'add'
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:10:45.180215 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:10:45.192134 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:10:45.202886 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:10:45.255301 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 17:10:45.256855 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 17:10:45.266679 4494439872 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:10:45.381976 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:10:45.388351 4494439872 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 30, 30, 32)        9248      
_________________________________________________________________
activation_2 (Activation)    (None, 30, 30, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 15, 15, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 15, 15, 32)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 15, 15, 64)        18496     
_________________________________________________________________
activation_3 (Activation)    (None, 15, 15, 64)        0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 13, 13, 64)        36928     
_________________________________________________________________
activation_4 (Activation)    (None, 13, 13, 64)        0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 6, 6, 64)          0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 6, 6, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 2304)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               1180160   
_________________________________________________________________
activation_5 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_6 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,250,858
Trainable params: 1,250,858
Non-trainable params: 0
_________________________________________________________________
W0626 17:10:45.524679 4494439872 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 17:10:45.912712: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 4s 5ms/step - loss: 2.1624 - categorical_crossentropy: 2.1624 - acc: 0.1889 - val_loss: 2.1579 - val_categorical_crossentropy: 2.1579 - val_acc: 0.1700
Epoch 2/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1534 - categorical_crossentropy: 2.1534 - acc: 0.1767 - val_loss: 2.2014 - val_categorical_crossentropy: 2.2014 - val_acc: 0.1600
Epoch 3/30
900/900 [==============================] - 4s 4ms/step - loss: 2.1177 - categorical_crossentropy: 2.1177 - acc: 0.1978 - val_loss: 2.1521 - val_categorical_crossentropy: 2.1521 - val_acc: 0.2400
Epoch 4/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1402 - categorical_crossentropy: 2.1402 - acc: 0.1856 - val_loss: 2.1579 - val_categorical_crossentropy: 2.1579 - val_acc: 0.1600
Epoch 5/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1229 - categorical_crossentropy: 2.1229 - acc: 0.2000 - val_loss: 2.2115 - val_categorical_crossentropy: 2.2115 - val_acc: 0.1600
Epoch 6/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1446 - categorical_crossentropy: 2.1446 - acc: 0.1933 - val_loss: 2.1570 - val_categorical_crossentropy: 2.1570 - val_acc: 0.0000e+00
Epoch 7/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1310 - categorical_crossentropy: 2.1310 - acc: 0.1856 - val_loss: 2.1482 - val_categorical_crossentropy: 2.1482 - val_acc: 0.0000e+00
Epoch 8/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1132 - categorical_crossentropy: 2.1132 - acc: 0.1956 - val_loss: 2.1233 - val_categorical_crossentropy: 2.1233 - val_acc: 0.1500
Epoch 9/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1031 - categorical_crossentropy: 2.1032 - acc: 0.2056 - val_loss: 2.1123 - val_categorical_crossentropy: 2.1124 - val_acc: 0.2200
Epoch 10/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0982 - categorical_crossentropy: 2.0982 - acc: 0.2111 - val_loss: 2.1045 - val_categorical_crossentropy: 2.1045 - val_acc: 0.2600
Epoch 11/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0745 - categorical_crossentropy: 2.0745 - acc: 0.2456 - val_loss: 2.0655 - val_categorical_crossentropy: 2.0655 - val_acc: 0.2900
Epoch 12/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0370 - categorical_crossentropy: 2.0370 - acc: 0.2600 - val_loss: 2.1779 - val_categorical_crossentropy: 2.1779 - val_acc: 0.1900
Epoch 13/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9989 - categorical_crossentropy: 1.9989 - acc: 0.2700 - val_loss: 2.0812 - val_categorical_crossentropy: 2.0812 - val_acc: 0.1900
Epoch 14/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9490 - categorical_crossentropy: 1.9491 - acc: 0.2900 - val_loss: 2.1286 - val_categorical_crossentropy: 2.1286 - val_acc: 0.2800
Epoch 15/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9038 - categorical_crossentropy: 1.9038 - acc: 0.2900 - val_loss: 2.0760 - val_categorical_crossentropy: 2.0760 - val_acc: 0.2900
Epoch 16/30
900/900 [==============================] - 3s 4ms/step - loss: 1.8312 - categorical_crossentropy: 1.8312 - acc: 0.3267 - val_loss: 2.1555 - val_categorical_crossentropy: 2.1555 - val_acc: 0.3100
Epoch 17/30
900/900 [==============================] - 3s 4ms/step - loss: 1.8292 - categorical_crossentropy: 1.8292 - acc: 0.3422 - val_loss: 2.1529 - val_categorical_crossentropy: 2.1529 - val_acc: 0.2900
Epoch 18/30
900/900 [==============================] - 3s 4ms/step - loss: 1.7448 - categorical_crossentropy: 1.7448 - acc: 0.3767 - val_loss: 2.3516 - val_categorical_crossentropy: 2.3516 - val_acc: 0.2200
Epoch 19/30
900/900 [==============================] - 3s 4ms/step - loss: 1.6884 - categorical_crossentropy: 1.6884 - acc: 0.3900 - val_loss: 2.2569 - val_categorical_crossentropy: 2.2570 - val_acc: 0.1800
Epoch 20/30
900/900 [==============================] - 3s 4ms/step - loss: 1.6470 - categorical_crossentropy: 1.6470 - acc: 0.4044 - val_loss: 2.4635 - val_categorical_crossentropy: 2.4635 - val_acc: 0.2200
Epoch 21/30
900/900 [==============================] - 3s 4ms/step - loss: 1.5712 - categorical_crossentropy: 1.5713 - acc: 0.4478 - val_loss: 2.5078 - val_categorical_crossentropy: 2.5078 - val_acc: 0.2300
Epoch 22/30
900/900 [==============================] - 3s 4ms/step - loss: 1.5223 - categorical_crossentropy: 1.5223 - acc: 0.4367 - val_loss: 2.5409 - val_categorical_crossentropy: 2.5410 - val_acc: 0.2000
Epoch 23/30
900/900 [==============================] - 3s 4ms/step - loss: 1.4441 - categorical_crossentropy: 1.4441 - acc: 0.4511 - val_loss: 2.4843 - val_categorical_crossentropy: 2.4843 - val_acc: 0.2100
Epoch 24/30
900/900 [==============================] - 3s 4ms/step - loss: 1.4295 - categorical_crossentropy: 1.4295 - acc: 0.4689 - val_loss: 2.5959 - val_categorical_crossentropy: 2.5959 - val_acc: 0.1800
Epoch 25/30
900/900 [==============================] - 3s 4ms/step - loss: 1.4207 - categorical_crossentropy: 1.4207 - acc: 0.4867 - val_loss: 2.6839 - val_categorical_crossentropy: 2.6839 - val_acc: 0.2000
Epoch 26/30
900/900 [==============================] - 3s 4ms/step - loss: 1.3062 - categorical_crossentropy: 1.3063 - acc: 0.4889 - val_loss: 2.7991 - val_categorical_crossentropy: 2.7991 - val_acc: 0.1900
Epoch 27/30
900/900 [==============================] - 4s 4ms/step - loss: 1.2661 - categorical_crossentropy: 1.2661 - acc: 0.5156 - val_loss: 3.3199 - val_categorical_crossentropy: 3.3199 - val_acc: 0.1800
Epoch 28/30
900/900 [==============================] - 3s 4ms/step - loss: 1.2363 - categorical_crossentropy: 1.2363 - acc: 0.5278 - val_loss: 3.1145 - val_categorical_crossentropy: 3.1145 - val_acc: 0.1900
Epoch 29/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1580 - categorical_crossentropy: 1.1580 - acc: 0.5433 - val_loss: 2.9061 - val_categorical_crossentropy: 2.9061 - val_acc: 0.1700
Epoch 30/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1448 - categorical_crossentropy: 1.1449 - acc: 0.5389 - val_loss: 3.3400 - val_categorical_crossentropy: 3.3400 - val_acc: 0.1600
train data:
1000/1000 [==============================] - 0s 420us/step
categorical_crossentropy :  1.0982732963562012

test data:
10000/10000 [==============================] - 4s 418us/step
acc :  0.201

test data:
10000/10000 [==============================] - 4s 412us/step
categorical_crossentropy :  2.950813561630249
acc :  0.201
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:13:48.031564 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:13:48.048875 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:13:48.053537 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:13:48.083217 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 17:13:48.084803 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 17:13:48.092754 4516554176 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:13:48.197355 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:13:48.203130 4516554176 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
activation_1 (Activation)    (None, 32, 32, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 30, 30, 32)        9248      
_________________________________________________________________
activation_2 (Activation)    (None, 30, 30, 32)        0         
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 15, 15, 32)        0         
_________________________________________________________________
dropout_1 (Dropout)          (None, 15, 15, 32)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 15, 15, 64)        18496     
_________________________________________________________________
activation_3 (Activation)    (None, 15, 15, 64)        0         
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 13, 13, 64)        36928     
_________________________________________________________________
activation_4 (Activation)    (None, 13, 13, 64)        0         
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 6, 6, 64)          0         
_________________________________________________________________
dropout_2 (Dropout)          (None, 6, 6, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 2304)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               1180160   
_________________________________________________________________
activation_5 (Activation)    (None, 512)               0         
_________________________________________________________________
dropout_3 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_6 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,250,858
Trainable params: 1,250,858
Non-trainable params: 0
_________________________________________________________________
W0626 17:13:48.298628 4516554176 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 17:13:48.667545: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 4s 4ms/step - loss: 2.1623 - categorical_crossentropy: 2.1623 - acc: 0.2044 - val_loss: 2.1414 - val_categorical_crossentropy: 2.1414 - val_acc: 0.1700
Epoch 2/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1365 - categorical_crossentropy: 2.1366 - acc: 0.1767 - val_loss: 2.1836 - val_categorical_crossentropy: 2.1836 - val_acc: 0.1600
Epoch 3/30
900/900 [==============================] - 3s 3ms/step - loss: 2.1305 - categorical_crossentropy: 2.1305 - acc: 0.1900 - val_loss: 2.1691 - val_categorical_crossentropy: 2.1691 - val_acc: 0.1600
Epoch 4/30
900/900 [==============================] - 3s 3ms/step - loss: 2.1235 - categorical_crossentropy: 2.1235 - acc: 0.1889 - val_loss: 2.0966 - val_categorical_crossentropy: 2.0966 - val_acc: 0.1600
Epoch 5/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1008 - categorical_crossentropy: 2.1008 - acc: 0.2078 - val_loss: 2.1146 - val_categorical_crossentropy: 2.1146 - val_acc: 0.3100
Epoch 6/30
900/900 [==============================] - 3s 4ms/step - loss: 2.1195 - categorical_crossentropy: 2.1195 - acc: 0.2122 - val_loss: 2.1045 - val_categorical_crossentropy: 2.1045 - val_acc: 0.2100
Epoch 7/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0928 - categorical_crossentropy: 2.0928 - acc: 0.2278 - val_loss: 2.1498 - val_categorical_crossentropy: 2.1499 - val_acc: 0.0500
Epoch 8/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0445 - categorical_crossentropy: 2.0445 - acc: 0.2433 - val_loss: 2.1232 - val_categorical_crossentropy: 2.1232 - val_acc: 0.2300
Epoch 9/30
900/900 [==============================] - 3s 4ms/step - loss: 2.0256 - categorical_crossentropy: 2.0256 - acc: 0.2467 - val_loss: 2.0317 - val_categorical_crossentropy: 2.0317 - val_acc: 0.2700
Epoch 10/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9573 - categorical_crossentropy: 1.9573 - acc: 0.2922 - val_loss: 2.1626 - val_categorical_crossentropy: 2.1626 - val_acc: 0.1900
Epoch 11/30
900/900 [==============================] - 3s 4ms/step - loss: 1.9140 - categorical_crossentropy: 1.9140 - acc: 0.2967 - val_loss: 2.0950 - val_categorical_crossentropy: 2.0950 - val_acc: 0.2800
Epoch 12/30
900/900 [==============================] - 3s 4ms/step - loss: 1.8403 - categorical_crossentropy: 1.8404 - acc: 0.3189 - val_loss: 2.2221 - val_categorical_crossentropy: 2.2221 - val_acc: 0.1800
Epoch 13/30
900/900 [==============================] - 3s 4ms/step - loss: 1.7707 - categorical_crossentropy: 1.7707 - acc: 0.3556 - val_loss: 2.3542 - val_categorical_crossentropy: 2.3542 - val_acc: 0.1300
Epoch 14/30
900/900 [==============================] - 3s 4ms/step - loss: 1.7038 - categorical_crossentropy: 1.7038 - acc: 0.3833 - val_loss: 2.1791 - val_categorical_crossentropy: 2.1792 - val_acc: 0.1600
Epoch 15/30
900/900 [==============================] - 3s 4ms/step - loss: 1.6677 - categorical_crossentropy: 1.6678 - acc: 0.4000 - val_loss: 2.3859 - val_categorical_crossentropy: 2.3859 - val_acc: 0.1900
Epoch 16/30
900/900 [==============================] - 3s 4ms/step - loss: 1.6098 - categorical_crossentropy: 1.6098 - acc: 0.4300 - val_loss: 2.4758 - val_categorical_crossentropy: 2.4758 - val_acc: 0.2000
Epoch 17/30
900/900 [==============================] - 4s 4ms/step - loss: 1.5862 - categorical_crossentropy: 1.5862 - acc: 0.4200 - val_loss: 2.3577 - val_categorical_crossentropy: 2.3577 - val_acc: 0.1900
Epoch 18/30
900/900 [==============================] - 4s 4ms/step - loss: 1.5109 - categorical_crossentropy: 1.5109 - acc: 0.4389 - val_loss: 2.4532 - val_categorical_crossentropy: 2.4533 - val_acc: 0.2000
Epoch 19/30
900/900 [==============================] - 3s 4ms/step - loss: 1.4353 - categorical_crossentropy: 1.4353 - acc: 0.4578 - val_loss: 2.5351 - val_categorical_crossentropy: 2.5351 - val_acc: 0.2200
Epoch 20/30
900/900 [==============================] - 4s 4ms/step - loss: 1.4303 - categorical_crossentropy: 1.4303 - acc: 0.4833 - val_loss: 2.6511 - val_categorical_crossentropy: 2.6512 - val_acc: 0.2300
Epoch 21/30
900/900 [==============================] - 3s 4ms/step - loss: 1.3607 - categorical_crossentropy: 1.3607 - acc: 0.4889 - val_loss: 3.0010 - val_categorical_crossentropy: 3.0011 - val_acc: 0.1600
Epoch 22/30
900/900 [==============================] - 3s 4ms/step - loss: 1.3054 - categorical_crossentropy: 1.3054 - acc: 0.4989 - val_loss: 2.9217 - val_categorical_crossentropy: 2.9217 - val_acc: 0.1800
Epoch 23/30
900/900 [==============================] - 4s 5ms/step - loss: 1.2744 - categorical_crossentropy: 1.2744 - acc: 0.5222 - val_loss: 3.0452 - val_categorical_crossentropy: 3.0453 - val_acc: 0.2100
Epoch 24/30
900/900 [==============================] - 4s 4ms/step - loss: 1.2174 - categorical_crossentropy: 1.2174 - acc: 0.5322 - val_loss: 3.3784 - val_categorical_crossentropy: 3.3784 - val_acc: 0.1900
Epoch 25/30
900/900 [==============================] - 4s 4ms/step - loss: 1.1706 - categorical_crossentropy: 1.1707 - acc: 0.5422 - val_loss: 3.4991 - val_categorical_crossentropy: 3.4991 - val_acc: 0.1500
Epoch 26/30
900/900 [==============================] - 3s 4ms/step - loss: 1.1569 - categorical_crossentropy: 1.1569 - acc: 0.5344 - val_loss: 3.1264 - val_categorical_crossentropy: 3.1265 - val_acc: 0.1900
Epoch 27/30
900/900 [==============================] - 4s 4ms/step - loss: 1.1019 - categorical_crossentropy: 1.1020 - acc: 0.5811 - val_loss: 3.4991 - val_categorical_crossentropy: 3.4991 - val_acc: 0.1800
Epoch 28/30
900/900 [==============================] - 4s 4ms/step - loss: 1.0903 - categorical_crossentropy: 1.0903 - acc: 0.5900 - val_loss: 3.4039 - val_categorical_crossentropy: 3.4039 - val_acc: 0.1800
Epoch 29/30
900/900 [==============================] - 3s 4ms/step - loss: 1.0666 - categorical_crossentropy: 1.0666 - acc: 0.5600 - val_loss: 3.4230 - val_categorical_crossentropy: 3.4230 - val_acc: 0.2100
Epoch 30/30
900/900 [==============================] - 4s 4ms/step - loss: 1.0184 - categorical_crossentropy: 1.0184 - acc: 0.5844 - val_loss: 3.4798 - val_categorical_crossentropy: 3.4798 - val_acc: 0.1600
train data:
1000/1000 [==============================] - 0s 411us/step
categorical_crossentropy :  1.01531929397583

test data:
10000/10000 [==============================] - 4s 412us/step
acc :  0.2009

test data:
10000/10000 [==============================] - 4s 410us/step
categorical_crossentropy :  3.1538935844421387
acc :  0.2009
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:17:53.364160 4630861248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

Traceback (most recent call last):
  File "imageBC.py", line 148, in <module>
    model = build_model( nb_classes=nb_classes, Wl20=1E-6, dr0=0.5, nb_features0=1024 )
  File "imageBC.py", line 41, in build_model
    model.add(Conv2D(nb_features, (3,3), padding='same', kernel_initializer='he_normal', kernel_regularizer=l2(Wl2), name=name, input_shape=(32,32,3)))
NameError: name 'l2' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:19:26.632593 4426823104 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:19:26.644543 4426823104 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:19:26.647695 4426823104 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4185: The name tf.truncated_normal is deprecated. Please use tf.random.truncated_normal instead.

Traceback (most recent call last):
  File "imageBC.py", line 148, in <module>
    model = build_model( nb_classes=nb_classes, Wl20=1E-6, dr0=0.5, nb_features0=1024 )
  File "imageBC.py", line 42, in build_model
    model.add( activation.afterConv2D(act, nb_features) )
NameError: name 'activation' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 27, in <module>
    sys.path.append('WiG/keras')
NameError: name 'sys' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:20:53.609246 4580185536 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:20:53.622420 4580185536 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:20:53.623857 4580185536 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4185: The name tf.truncated_normal is deprecated. Please use tf.random.truncated_normal instead.

Traceback (most recent call last):
  File "imageBC.py", line 152, in <module>
    model = build_model( nb_classes=nb_classes, Wl20=1E-6, dr0=0.5, nb_features0=1024 )
  File "imageBC.py", line 50, in build_model
    model.add(SpatialDropout2D(dropout))
NameError: name 'SpatialDropout2D' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:21:32.387811 4410832320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:21:32.400195 4410832320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:21:32.425562 4410832320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4185: The name tf.truncated_normal is deprecated. Please use tf.random.truncated_normal instead.

W0626 17:21:32.496271 4410832320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 17:21:32.511529 4410832320 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:21:32.857558 4410832320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:21:32.862682 4410832320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

W0626 17:21:33.153888 4410832320 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 17:21:34.033253: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 41s 46ms/step - loss: 2.6432 - categorical_crossentropy: 2.6380 - acc: 0.1711 - val_loss: 2.2140 - val_categorical_crossentropy: 2.2088 - val_acc: 0.0000e+00
Epoch 2/30
900/900 [==============================] - 38s 42ms/step - loss: 2.1776 - categorical_crossentropy: 2.1725 - acc: 0.1967 - val_loss: 2.1931 - val_categorical_crossentropy: 2.1881 - val_acc: 0.1600
Epoch 3/30
900/900 [==============================] - 38s 42ms/step - loss: 2.1495 - categorical_crossentropy: 2.1445 - acc: 0.1822 - val_loss: 2.1567 - val_categorical_crossentropy: 2.1517 - val_acc: 0.1600
Epoch 4/30
900/900 [==============================] - 43s 48ms/step - loss: 2.1487 - categorical_crossentropy: 2.1437 - acc: 0.1689 - val_loss: 2.1484 - val_categorical_crossentropy: 2.1433 - val_acc: 0.0100
Epoch 5/30
160/900 [====>.........................] - ETA: 31s - loss: 2.1418 - categorical_crossentropy: 2.1368 - acc: 0.2063^CTraceback (most recent call last):
  File "imageBC.py", line 154, in <module>
    result = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,verbose=1)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training.py", line 1039, in fit
    validation_steps=validation_steps)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training_arrays.py", line 199, in fit_loop
    outs = f(ins_batch)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2715, in __call__
    return self._call(inputs)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2675, in _call
    fetched = self._callable_fn(*array_vals)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1458, in __call__
    run_metadata_ptr)
KeyboardInterrupt
^C
^C
(test) YaCnoMacBook-puro:train1000-master shoichi$ 
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
^CTraceback (most recent call last):
  File "imageBC.py", line 14, in <module>
    import data
  File "/Users/shoichi/Desktop/research_git/train1000-master/data.py", line 4, in <module>
    from keras import backend as K
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/__init__.py", line 3, in <module>
    from . import utils
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/utils/__init__.py", line 6, in <module>
    from . import conv_utils
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/utils/conv_utils.py", line 9, in <module>
    from .. import backend as K
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/__init__.py", line 89, in <module>
    from .tensorflow_backend import *
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 5, in <module>
    import tensorflow as tf
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/__init__.py", line 28, in <module>
    from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/__init__.py", line 83, in <module>
    from tensorflow.python import keras
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/keras/__init__.py", line 32, in <module>
    from tensorflow.python.keras import datasets
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/keras/datasets/__init__.py", line 25, in <module>
    from tensorflow.python.keras.datasets import imdb
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/keras/datasets/imdb.py", line 25, in <module>
    from tensorflow.python.keras.preprocessing.sequence import _remove_long_seq
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/keras/preprocessing/__init__.py", line 30, in <module>
    from tensorflow.python.keras.preprocessing import image
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/keras/preprocessing/image.py", line 23, in <module>
    from keras_preprocessing import image
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras_preprocessing/image/__init__.py", line 5, in <module>
    from .affine_transformations import *
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras_preprocessing/image/affine_transformations.py", line 9, in <module>
    from .utils import (array_to_img,
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras_preprocessing/image/utils.py", line 13, in <module>
    from PIL import ImageEnhance
  File "<frozen importlib._bootstrap>", line 1032, in _handle_fromlist
KeyboardInterrupt
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:28:40.918869 4591646144 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:28:40.930298 4591646144 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:28:40.931659 4591646144 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4185: The name tf.truncated_normal is deprecated. Please use tf.random.truncated_normal instead.

W0626 17:28:40.949906 4591646144 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 17:28:40.954842 4591646144 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:28:41.270352 4591646144 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:28:41.275352 4591646144 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

W0626 17:28:41.474074 4591646144 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/10
2019-06-26 17:28:42.304328: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 39s 44ms/step - loss: 13.1524 - categorical_crossentropy: 13.1474 - acc: 0.1767 - val_loss: 16.1227 - val_categorical_crossentropy: 16.1181 - val_acc: 0.0000e+00
Epoch 2/10
900/900 [==============================] - 37s 41ms/step - loss: 13.2032 - categorical_crossentropy: 13.1989 - acc: 0.1811 - val_loss: 16.1220 - val_categorical_crossentropy: 16.1181 - val_acc: 0.0000e+00
Epoch 3/10
900/900 [==============================] - 37s 41ms/step - loss: 13.2027 - categorical_crossentropy: 13.1989 - acc: 0.1811 - val_loss: 16.1218 - val_categorical_crossentropy: 16.1181 - val_acc: 0.0000e+00
Epoch 4/10
900/900 [==============================] - 37s 41ms/step - loss: 13.2026 - categorical_crossentropy: 13.1989 - acc: 0.1811 - val_loss: 16.1217 - val_categorical_crossentropy: 16.1181 - val_acc: 0.0000e+00
Epoch 5/10
900/900 [==============================] - 36s 40ms/step - loss: 13.2025 - categorical_crossentropy: 13.1989 - acc: 0.1811 - val_loss: 16.1217 - val_categorical_crossentropy: 16.1181 - val_acc: 0.0000e+00
Epoch 6/10
900/900 [==============================] - 37s 41ms/step - loss: 13.2025 - categorical_crossentropy: 13.1989 - acc: 0.1811 - val_loss: 16.1217 - val_categorical_crossentropy: 16.1181 - val_acc: 0.0000e+00
Epoch 7/10
 60/900 [=>............................] - ETA: 33s - loss: 13.4353 - categorical_crossentropy: 13.4317 - acc: 0.1667^CTraceback (most recent call last):
  File "imageBC.py", line 154, in <module>
    result = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,verbose=1)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training.py", line 1039, in fit
    validation_steps=validation_steps)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/engine/training_arrays.py", line 199, in fit_loop
    outs = f(ins_batch)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2715, in __call__
    return self._call(inputs)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 2675, in _call
    fetched = self._callable_fn(*array_vals)
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/client/session.py", line 1458, in __call__
    run_metadata_ptr)
KeyboardInterrupt
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ ls
README.md		c.png			e.png			sample			sample_cifar10.py	test			wig_ensemble_cifar.py
WiG			d.png			get_models.sh		sample1.png		sample_cifar100.py	train1000.py		wig_ensemble_mnist.py
__pycache__		data.py			imageBC.py		sample2.png		sample_mnist.csv	trainwith1000result.txt
a.png			demon1.png		my1000sample.py		sample_cifar10.csv	sample_mnist.hdf5	untitled2.py
b.png			demon2.png		myTrainwith1000.py	sample_cifar10.hdf5	sample_mnist.py		untitled4.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python sample_cifar19.py
/usr/local/Cellar/python/3.7.2_2/Frameworks/Python.framework/Versions/3.7/Resources/Python.app/Contents/MacOS/Python: can't open file 'sample_cifar19.py': [Errno 2] No such file or directory
(test) YaCnoMacBook-puro:train1000-master shoichi$ python sample_cifar10.py
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:33:54.780280 4313089472 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:33:54.791588 4313089472 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:33:54.792836 4313089472 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4185: The name tf.truncated_normal is deprecated. Please use tf.random.truncated_normal instead.

W0626 17:33:54.810756 4313089472 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 17:33:54.817214 4313089472 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:33:55.165607 4313089472 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:33:55.170429 4313089472 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

2019-06-26 17:33:55.488271: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
train data:
categorical_crossentropy :  2.188026290893555
acc :  0.187

test data:
categorical_crossentropy :  2.2081976974487305
acc :  0.1727
(test) YaCnoMacBook-puro:train1000-master shoichi$ ls
README.md		c.png			e.png			sample			sample_cifar10.py	test			wig_ensemble_cifar.py
WiG			d.png			get_models.sh		sample1.png		sample_cifar100.py	train1000.py		wig_ensemble_mnist.py
__pycache__		data.py			imageBC.py		sample2.png		sample_mnist.csv	trainwith1000result.txt
a.png			demon1.png		my1000sample.py		sample_cifar10.csv	sample_mnist.hdf5	untitled2.py
b.png			demon2.png		myTrainwith1000.py	sample_cifar10.hdf5	sample_mnist.py		untitled4.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python sample_mnist.py
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:35:02.049182 4454045120 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:35:02.060954 4454045120 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:35:02.068164 4454045120 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:35:02.125827 4454045120 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 17:35:02.155738 4454045120 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:35:02.191418 4454045120 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:35:02.200500 4454045120 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

2019-06-26 17:35:02.246666: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
train data:
categorical_crossentropy :  0.19672523021698
acc :  0.951

test data:
categorical_crossentropy :  0.3485072293102741
acc :  0.8932
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim sample_mnist.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:38:21.898405 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:38:21.909528 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:38:21.914762 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:38:21.932225 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:174: The name tf.get_default_session is deprecated. Please use tf.compat.v1.get_default_session instead.

W0626 17:38:21.932366 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:181: The name tf.ConfigProto is deprecated. Please use tf.compat.v1.ConfigProto instead.

2019-06-26 17:38:21.932616: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
W0626 17:38:21.952877 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1834: The name tf.nn.fused_batch_norm is deprecated. Please use tf.compat.v1.nn.fused_batch_norm instead.

W0626 17:38:23.810117 4711814592 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 17:38:23.810333 4711814592 nn_ops.py:4224] Large dropout rate: 0.7 (>0.5). In TensorFlow 2.x, dropout() uses dropout rate instead of keep_prob. Please ensure that this is intended.
_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
input_1 (InputLayer)         (None, 32, 32, 3)         0         
_________________________________________________________________
conv1_pad (ZeroPadding2D)    (None, 33, 33, 3)         0         
_________________________________________________________________
conv1 (Conv2D)               (None, 16, 16, 32)        864       
_________________________________________________________________
conv1_bn (BatchNormalization (None, 16, 16, 32)        128       
_________________________________________________________________
conv1_relu (ReLU)            (None, 16, 16, 32)        0         
_________________________________________________________________
conv_dw_1 (DepthwiseConv2D)  (None, 16, 16, 32)        288       
_________________________________________________________________
conv_dw_1_bn (BatchNormaliza (None, 16, 16, 32)        128       
_________________________________________________________________
conv_dw_1_relu (ReLU)        (None, 16, 16, 32)        0         
_________________________________________________________________
conv_pw_1 (Conv2D)           (None, 16, 16, 64)        2048      
_________________________________________________________________
conv_pw_1_bn (BatchNormaliza (None, 16, 16, 64)        256       
_________________________________________________________________
conv_pw_1_relu (ReLU)        (None, 16, 16, 64)        0         
_________________________________________________________________
conv_pad_2 (ZeroPadding2D)   (None, 17, 17, 64)        0         
_________________________________________________________________
conv_dw_2 (DepthwiseConv2D)  (None, 8, 8, 64)          576       
_________________________________________________________________
conv_dw_2_bn (BatchNormaliza (None, 8, 8, 64)          256       
_________________________________________________________________
conv_dw_2_relu (ReLU)        (None, 8, 8, 64)          0         
_________________________________________________________________
conv_pw_2 (Conv2D)           (None, 8, 8, 128)         8192      
_________________________________________________________________
conv_pw_2_bn (BatchNormaliza (None, 8, 8, 128)         512       
_________________________________________________________________
conv_pw_2_relu (ReLU)        (None, 8, 8, 128)         0         
_________________________________________________________________
conv_dw_3 (DepthwiseConv2D)  (None, 8, 8, 128)         1152      
_________________________________________________________________
conv_dw_3_bn (BatchNormaliza (None, 8, 8, 128)         512       
_________________________________________________________________
conv_dw_3_relu (ReLU)        (None, 8, 8, 128)         0         
_________________________________________________________________
conv_pw_3 (Conv2D)           (None, 8, 8, 128)         16384     
_________________________________________________________________
conv_pw_3_bn (BatchNormaliza (None, 8, 8, 128)         512       
_________________________________________________________________
conv_pw_3_relu (ReLU)        (None, 8, 8, 128)         0         
_________________________________________________________________
conv_pad_4 (ZeroPadding2D)   (None, 9, 9, 128)         0         
_________________________________________________________________
conv_dw_4 (DepthwiseConv2D)  (None, 4, 4, 128)         1152      
_________________________________________________________________
conv_dw_4_bn (BatchNormaliza (None, 4, 4, 128)         512       
_________________________________________________________________
conv_dw_4_relu (ReLU)        (None, 4, 4, 128)         0         
_________________________________________________________________
conv_pw_4 (Conv2D)           (None, 4, 4, 256)         32768     
_________________________________________________________________
conv_pw_4_bn (BatchNormaliza (None, 4, 4, 256)         1024      
_________________________________________________________________
conv_pw_4_relu (ReLU)        (None, 4, 4, 256)         0         
_________________________________________________________________
conv_dw_5 (DepthwiseConv2D)  (None, 4, 4, 256)         2304      
_________________________________________________________________
conv_dw_5_bn (BatchNormaliza (None, 4, 4, 256)         1024      
_________________________________________________________________
conv_dw_5_relu (ReLU)        (None, 4, 4, 256)         0         
_________________________________________________________________
conv_pw_5 (Conv2D)           (None, 4, 4, 256)         65536     
_________________________________________________________________
conv_pw_5_bn (BatchNormaliza (None, 4, 4, 256)         1024      
_________________________________________________________________
conv_pw_5_relu (ReLU)        (None, 4, 4, 256)         0         
_________________________________________________________________
conv_pad_6 (ZeroPadding2D)   (None, 5, 5, 256)         0         
_________________________________________________________________
conv_dw_6 (DepthwiseConv2D)  (None, 2, 2, 256)         2304      
_________________________________________________________________
conv_dw_6_bn (BatchNormaliza (None, 2, 2, 256)         1024      
_________________________________________________________________
conv_dw_6_relu (ReLU)        (None, 2, 2, 256)         0         
_________________________________________________________________
conv_pw_6 (Conv2D)           (None, 2, 2, 512)         131072    
_________________________________________________________________
conv_pw_6_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_6_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_7 (DepthwiseConv2D)  (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_7_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_7_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_7 (Conv2D)           (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_7_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_7_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_8 (DepthwiseConv2D)  (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_8_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_8_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_8 (Conv2D)           (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_8_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_8_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_9 (DepthwiseConv2D)  (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_9_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_9_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_9 (Conv2D)           (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_9_bn (BatchNormaliza (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_9_relu (ReLU)        (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_10 (DepthwiseConv2D) (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_10_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_10_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_10 (Conv2D)          (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_10_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_10_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_dw_11 (DepthwiseConv2D) (None, 2, 2, 512)         4608      
_________________________________________________________________
conv_dw_11_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_dw_11_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pw_11 (Conv2D)          (None, 2, 2, 512)         262144    
_________________________________________________________________
conv_pw_11_bn (BatchNormaliz (None, 2, 2, 512)         2048      
_________________________________________________________________
conv_pw_11_relu (ReLU)       (None, 2, 2, 512)         0         
_________________________________________________________________
conv_pad_12 (ZeroPadding2D)  (None, 3, 3, 512)         0         
_________________________________________________________________
conv_dw_12 (DepthwiseConv2D) (None, 1, 1, 512)         4608      
_________________________________________________________________
conv_dw_12_bn (BatchNormaliz (None, 1, 1, 512)         2048      
_________________________________________________________________
conv_dw_12_relu (ReLU)       (None, 1, 1, 512)         0         
_________________________________________________________________
conv_pw_12 (Conv2D)          (None, 1, 1, 1024)        524288    
_________________________________________________________________
conv_pw_12_bn (BatchNormaliz (None, 1, 1, 1024)        4096      
_________________________________________________________________
conv_pw_12_relu (ReLU)       (None, 1, 1, 1024)        0         
_________________________________________________________________
conv_dw_13 (DepthwiseConv2D) (None, 1, 1, 1024)        9216      
_________________________________________________________________
conv_dw_13_bn (BatchNormaliz (None, 1, 1, 1024)        4096      
_________________________________________________________________
conv_dw_13_relu (ReLU)       (None, 1, 1, 1024)        0         
_________________________________________________________________
conv_pw_13 (Conv2D)          (None, 1, 1, 1024)        1048576   
_________________________________________________________________
conv_pw_13_bn (BatchNormaliz (None, 1, 1, 1024)        4096      
_________________________________________________________________
conv_pw_13_relu (ReLU)       (None, 1, 1, 1024)        0         
_________________________________________________________________
global_average_pooling2d_1 ( (None, 1024)              0         
_________________________________________________________________
reshape_1 (Reshape)          (None, 1, 1, 1024)        0         
_________________________________________________________________
dropout (Dropout)            (None, 1, 1, 1024)        0         
_________________________________________________________________
conv_preds (Conv2D)          (None, 1, 1, 10)          10250     
_________________________________________________________________
reshape_2 (Reshape)          (None, 10)                0         
_________________________________________________________________
act_softmax (Activation)     (None, 10)                0         
=================================================================
Total params: 3,239,114
Trainable params: 3,217,226
Non-trainable params: 21,888
_________________________________________________________________
W0626 17:38:23.864181 4711814592 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:38:23.980270 4711814592 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/10
900/900 [==============================] - 13s 14ms/step - loss: 3.2719 - categorical_crossentropy: 3.2719 - acc: 0.1378 - val_loss: 5.6528 - val_categorical_crossentropy: 5.6528 - val_acc: 0.1100
Epoch 2/10
900/900 [==============================] - 9s 10ms/step - loss: 2.7683 - categorical_crossentropy: 2.7683 - acc: 0.1756 - val_loss: 3.2998 - val_categorical_crossentropy: 3.2998 - val_acc: 0.1400
Epoch 3/10
900/900 [==============================] - 9s 10ms/step - loss: 2.7738 - categorical_crossentropy: 2.7738 - acc: 0.1644 - val_loss: 2.5777 - val_categorical_crossentropy: 2.5777 - val_acc: 0.1200
Epoch 4/10
900/900 [==============================] - 9s 10ms/step - loss: 2.6121 - categorical_crossentropy: 2.6121 - acc: 0.1833 - val_loss: 2.2719 - val_categorical_crossentropy: 2.2719 - val_acc: 0.0800
Epoch 5/10
900/900 [==============================] - 9s 10ms/step - loss: 2.6785 - categorical_crossentropy: 2.6785 - acc: 0.1756 - val_loss: 3.6382 - val_categorical_crossentropy: 3.6382 - val_acc: 0.0800
Epoch 6/10
900/900 [==============================] - 9s 10ms/step - loss: 2.6606 - categorical_crossentropy: 2.6606 - acc: 0.1711 - val_loss: 2.7410 - val_categorical_crossentropy: 2.7410 - val_acc: 0.1100
Epoch 7/10
900/900 [==============================] - 9s 10ms/step - loss: 2.4584 - categorical_crossentropy: 2.4584 - acc: 0.2144 - val_loss: 2.2705 - val_categorical_crossentropy: 2.2705 - val_acc: 0.1300
Epoch 8/10
900/900 [==============================] - 9s 10ms/step - loss: 2.4608 - categorical_crossentropy: 2.4608 - acc: 0.2456 - val_loss: 2.4077 - val_categorical_crossentropy: 2.4077 - val_acc: 0.1500
Epoch 9/10
900/900 [==============================] - 9s 10ms/step - loss: 2.4064 - categorical_crossentropy: 2.4064 - acc: 0.2667 - val_loss: 2.4774 - val_categorical_crossentropy: 2.4774 - val_acc: 0.1700
Epoch 10/10
900/900 [==============================] - 9s 10ms/step - loss: 2.3626 - categorical_crossentropy: 2.3626 - acc: 0.2500 - val_loss: 2.3262 - val_categorical_crossentropy: 2.3262 - val_acc: 0.1700
train data:
1000/1000 [==============================] - 1s 1ms/step
categorical_crossentropy :  2.1072502899169923

test data:
10000/10000 [==============================] - 11s 1ms/step
acc :  0.1557

test data:
10000/10000 [==============================] - 13s 1ms/step
categorical_crossentropy :  2.8474905754089357
acc :  0.1557
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 25, in <module>
    sys.path.append('WiG/keras')
NameError: name 'sys' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:45:14.653005 4651075008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

Traceback (most recent call last):
  File "imageBC.py", line 73, in <module>
    model = model()
  File "imageBC.py", line 27, in model
    model.add(Conv2D(32, kernel_size=3, padding="same", input_shape=self.shape,activation="relu"))                                            #畳み込み１層目
NameError: name 'self' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:46:06.422199 4545873344 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:46:06.434675 4545873344 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:46:06.436380 4545873344 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:46:06.448773 4545873344 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

Traceback (most recent call last):
  File "imageBC.py", line 73, in <module>
    model = model()
  File "imageBC.py", line 33, in model
    model.add(Dense(self.output_size))                                              #全結合2層目
NameError: name 'self' is not defined
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:46:28.488519 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:46:28.500494 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:46:28.502228 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:46:28.513401 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:46:28.566468 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:46:28.571151 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

W0626 17:46:28.654798 4650104256 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:46:28.706710 4650104256 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/10
2019-06-26 17:46:28.877100: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 3s 3ms/step - loss: 2.1513 - categorical_crossentropy: 2.1513 - acc: 0.1889 - val_loss: 2.0759 - val_categorical_crossentropy: 2.0759 - val_acc: 0.2900
Epoch 2/10
900/900 [==============================] - 2s 2ms/step - loss: 2.0881 - categorical_crossentropy: 2.0881 - acc: 0.2211 - val_loss: 2.0738 - val_categorical_crossentropy: 2.0738 - val_acc: 0.1900
Epoch 3/10
900/900 [==============================] - 2s 2ms/step - loss: 2.0245 - categorical_crossentropy: 2.0245 - acc: 0.2733 - val_loss: 2.1531 - val_categorical_crossentropy: 2.1531 - val_acc: 0.2400
Epoch 4/10
900/900 [==============================] - 2s 2ms/step - loss: 1.9062 - categorical_crossentropy: 1.9062 - acc: 0.3233 - val_loss: 2.1697 - val_categorical_crossentropy: 2.1697 - val_acc: 0.1900
Epoch 5/10
900/900 [==============================] - 2s 2ms/step - loss: 1.7873 - categorical_crossentropy: 1.7873 - acc: 0.3789 - val_loss: 2.0156 - val_categorical_crossentropy: 2.0156 - val_acc: 0.2700
Epoch 6/10
900/900 [==============================] - 2s 2ms/step - loss: 1.6660 - categorical_crossentropy: 1.6660 - acc: 0.3900 - val_loss: 2.3216 - val_categorical_crossentropy: 2.3216 - val_acc: 0.2200
Epoch 7/10
900/900 [==============================] - 2s 2ms/step - loss: 1.5697 - categorical_crossentropy: 1.5697 - acc: 0.4300 - val_loss: 2.1957 - val_categorical_crossentropy: 2.1957 - val_acc: 0.2300
Epoch 8/10
900/900 [==============================] - 2s 2ms/step - loss: 1.4550 - categorical_crossentropy: 1.4550 - acc: 0.4578 - val_loss: 2.5428 - val_categorical_crossentropy: 2.5428 - val_acc: 0.1900
Epoch 9/10
900/900 [==============================] - 2s 2ms/step - loss: 1.3571 - categorical_crossentropy: 1.3571 - acc: 0.4933 - val_loss: 2.7870 - val_categorical_crossentropy: 2.7870 - val_acc: 0.1800
Epoch 10/10
900/900 [==============================] - 2s 2ms/step - loss: 1.2873 - categorical_crossentropy: 1.2873 - acc: 0.5122 - val_loss: 2.7873 - val_categorical_crossentropy: 2.7873 - val_acc: 0.1300
train data:
1000/1000 [==============================] - 0s 211us/step
categorical_crossentropy :  1.3293267707824707

test data:
10000/10000 [==============================] - 2s 212us/step
acc :  0.2195

test data:
10000/10000 [==============================] - 2s 217us/step
categorical_crossentropy :  2.5933115505218507
acc :  0.2195
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:48:46.387716 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:48:46.400260 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:48:46.401875 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:48:46.412970 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:48:46.466408 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:48:46.471034 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3295: The name tf.log is deprecated. Please use tf.math.log instead.

W0626 17:48:46.554389 4554220992 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:48:46.606118 4554220992 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/10
2019-06-26 17:48:46.778719: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 3s 3ms/step - loss: 2.1706 - categorical_crossentropy: 2.1706 - acc: 0.1744 - val_loss: 2.1576 - val_categorical_crossentropy: 2.1576 - val_acc: 0.1600
Epoch 2/10
900/900 [==============================] - 2s 2ms/step - loss: 2.1170 - categorical_crossentropy: 2.1170 - acc: 0.1989 - val_loss: 2.1663 - val_categorical_crossentropy: 2.1663 - val_acc: 0.0000e+00
Epoch 3/10
900/900 [==============================] - 2s 2ms/step - loss: 2.0367 - categorical_crossentropy: 2.0367 - acc: 0.2511 - val_loss: 2.1606 - val_categorical_crossentropy: 2.1606 - val_acc: 0.1400
Epoch 4/10
900/900 [==============================] - 2s 2ms/step - loss: 1.9282 - categorical_crossentropy: 1.9282 - acc: 0.3056 - val_loss: 2.0449 - val_categorical_crossentropy: 2.0449 - val_acc: 0.2800
Epoch 5/10
900/900 [==============================] - 2s 2ms/step - loss: 1.7820 - categorical_crossentropy: 1.7820 - acc: 0.3789 - val_loss: 2.0792 - val_categorical_crossentropy: 2.0792 - val_acc: 0.2400
Epoch 6/10
900/900 [==============================] - 2s 2ms/step - loss: 1.6499 - categorical_crossentropy: 1.6499 - acc: 0.4067 - val_loss: 2.5230 - val_categorical_crossentropy: 2.5230 - val_acc: 0.1900
Epoch 7/10
900/900 [==============================] - 2s 2ms/step - loss: 1.5158 - categorical_crossentropy: 1.5158 - acc: 0.4444 - val_loss: 2.2684 - val_categorical_crossentropy: 2.2684 - val_acc: 0.2300
Epoch 8/10
900/900 [==============================] - 2s 3ms/step - loss: 1.4735 - categorical_crossentropy: 1.4735 - acc: 0.4522 - val_loss: 2.4399 - val_categorical_crossentropy: 2.4399 - val_acc: 0.2400
Epoch 9/10
900/900 [==============================] - 2s 2ms/step - loss: 1.3610 - categorical_crossentropy: 1.3610 - acc: 0.4911 - val_loss: 2.8685 - val_categorical_crossentropy: 2.8685 - val_acc: 0.2300
Epoch 10/10
900/900 [==============================] - 2s 2ms/step - loss: 1.2735 - categorical_crossentropy: 1.2735 - acc: 0.4800 - val_loss: 3.0991 - val_categorical_crossentropy: 3.0991 - val_acc: 0.2200
train data:
1000/1000 [==============================] - 0s 221us/step
categorical_crossentropy :  1.331233783721924

test data:
10000/10000 [==============================] - 2s 215us/step
acc :  0.1933

test data:
10000/10000 [==============================] - 2s 229us/step
categorical_crossentropy :  2.957813939666748
acc :  0.1933
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:50:28.347994 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:50:28.360235 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:50:28.361818 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:50:28.373965 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:50:28.426006 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:50:28.430977 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

W0626 17:50:28.520678 4753593792 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:50:28.552050 4753593792 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/10
2019-06-26 17:50:28.719894: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 2s 3ms/step - loss: 2.1516 - kullback_leibler_divergence: 2.1516 - acc: 0.1967 - val_loss: 2.1122 - val_kullback_leibler_divergence: 2.1122 - val_acc: 0.1600
Epoch 2/10
900/900 [==============================] - 2s 2ms/step - loss: 2.0884 - kullback_leibler_divergence: 2.0884 - acc: 0.2422 - val_loss: 2.0899 - val_kullback_leibler_divergence: 2.0899 - val_acc: 0.3500
Epoch 3/10
900/900 [==============================] - 2s 2ms/step - loss: 1.9980 - kullback_leibler_divergence: 1.9980 - acc: 0.2878 - val_loss: 2.2205 - val_kullback_leibler_divergence: 2.2205 - val_acc: 0.1200
Epoch 4/10
900/900 [==============================] - 2s 2ms/step - loss: 1.8612 - kullback_leibler_divergence: 1.8612 - acc: 0.3356 - val_loss: 2.1011 - val_kullback_leibler_divergence: 2.1011 - val_acc: 0.1800
Epoch 5/10
900/900 [==============================] - 2s 2ms/step - loss: 1.7134 - kullback_leibler_divergence: 1.7134 - acc: 0.3989 - val_loss: 2.3763 - val_kullback_leibler_divergence: 2.3763 - val_acc: 0.2200
Epoch 6/10
900/900 [==============================] - 2s 2ms/step - loss: 1.6119 - kullback_leibler_divergence: 1.6119 - acc: 0.4311 - val_loss: 2.4002 - val_kullback_leibler_divergence: 2.4002 - val_acc: 0.2000
Epoch 7/10
900/900 [==============================] - 2s 2ms/step - loss: 1.4933 - kullback_leibler_divergence: 1.4933 - acc: 0.4633 - val_loss: 2.3687 - val_kullback_leibler_divergence: 2.3687 - val_acc: 0.2100
Epoch 8/10
900/900 [==============================] - 2s 2ms/step - loss: 1.3972 - kullback_leibler_divergence: 1.3972 - acc: 0.4544 - val_loss: 2.6537 - val_kullback_leibler_divergence: 2.6537 - val_acc: 0.1400
Epoch 9/10
900/900 [==============================] - 2s 2ms/step - loss: 1.3413 - kullback_leibler_divergence: 1.3413 - acc: 0.4833 - val_loss: 2.6604 - val_kullback_leibler_divergence: 2.6604 - val_acc: 0.2100
Epoch 10/10
900/900 [==============================] - 2s 2ms/step - loss: 1.2513 - kullback_leibler_divergence: 1.2513 - acc: 0.5144 - val_loss: 3.0882 - val_kullback_leibler_divergence: 3.0882 - val_acc: 0.1900
train data:
1000/1000 [==============================] - 0s 227us/step
kullback_leibler_divergence :  1.260401128768921

test data:
10000/10000 [==============================] - 2s 225us/step
acc :  0.2083

test data:
10000/10000 [==============================] - 2s 222us/step
kullback_leibler_divergence :  2.96919889755249
acc :  0.2083
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:51:23.912550 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:51:23.925219 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:51:23.926906 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:51:23.938265 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:51:23.990821 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:51:23.996112 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

W0626 17:51:24.084101 4662937024 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:51:24.114586 4662937024 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 17:51:24.280616: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 3s 3ms/step - loss: 2.1520 - kullback_leibler_divergence: 2.1520 - acc: 0.2067 - val_loss: 2.2396 - val_kullback_leibler_divergence: 2.2396 - val_acc: 0.1200
Epoch 2/30
900/900 [==============================] - 2s 2ms/step - loss: 2.0994 - kullback_leibler_divergence: 2.0994 - acc: 0.2389 - val_loss: 2.1466 - val_kullback_leibler_divergence: 2.1466 - val_acc: 0.1800
Epoch 3/30
900/900 [==============================] - 2s 2ms/step - loss: 2.0234 - kullback_leibler_divergence: 2.0234 - acc: 0.2567 - val_loss: 2.0536 - val_kullback_leibler_divergence: 2.0536 - val_acc: 0.2800
Epoch 4/30
900/900 [==============================] - 2s 2ms/step - loss: 1.9038 - kullback_leibler_divergence: 1.9038 - acc: 0.3067 - val_loss: 2.0835 - val_kullback_leibler_divergence: 2.0835 - val_acc: 0.2700
Epoch 5/30
900/900 [==============================] - 2s 2ms/step - loss: 1.7853 - kullback_leibler_divergence: 1.7853 - acc: 0.3689 - val_loss: 2.1676 - val_kullback_leibler_divergence: 2.1676 - val_acc: 0.3000
Epoch 6/30
900/900 [==============================] - 2s 2ms/step - loss: 1.6551 - kullback_leibler_divergence: 1.6551 - acc: 0.4222 - val_loss: 2.4017 - val_kullback_leibler_divergence: 2.4017 - val_acc: 0.2400
Epoch 7/30
900/900 [==============================] - 2s 2ms/step - loss: 1.5489 - kullback_leibler_divergence: 1.5489 - acc: 0.4467 - val_loss: 2.3495 - val_kullback_leibler_divergence: 2.3495 - val_acc: 0.2600
Epoch 8/30
900/900 [==============================] - 2s 2ms/step - loss: 1.4453 - kullback_leibler_divergence: 1.4453 - acc: 0.4567 - val_loss: 2.7244 - val_kullback_leibler_divergence: 2.7244 - val_acc: 0.1000
Epoch 9/30
900/900 [==============================] - 2s 2ms/step - loss: 1.3375 - kullback_leibler_divergence: 1.3375 - acc: 0.4711 - val_loss: 2.6394 - val_kullback_leibler_divergence: 2.6394 - val_acc: 0.1400
Epoch 10/30
900/900 [==============================] - 2s 2ms/step - loss: 1.2928 - kullback_leibler_divergence: 1.2928 - acc: 0.4922 - val_loss: 2.8973 - val_kullback_leibler_divergence: 2.8973 - val_acc: 0.2200
Epoch 11/30
900/900 [==============================] - 2s 2ms/step - loss: 1.2090 - kullback_leibler_divergence: 1.2090 - acc: 0.5267 - val_loss: 3.3333 - val_kullback_leibler_divergence: 3.3333 - val_acc: 0.1400
Epoch 12/30
900/900 [==============================] - 2s 2ms/step - loss: 1.1350 - kullback_leibler_divergence: 1.1350 - acc: 0.5456 - val_loss: 3.2268 - val_kullback_leibler_divergence: 3.2268 - val_acc: 0.2200
Epoch 13/30
900/900 [==============================] - 2s 2ms/step - loss: 1.0837 - kullback_leibler_divergence: 1.0837 - acc: 0.5333 - val_loss: 3.4658 - val_kullback_leibler_divergence: 3.4658 - val_acc: 0.1900
Epoch 14/30
900/900 [==============================] - 2s 2ms/step - loss: 1.0489 - kullback_leibler_divergence: 1.0489 - acc: 0.5489 - val_loss: 3.6035 - val_kullback_leibler_divergence: 3.6035 - val_acc: 0.2200
Epoch 15/30
900/900 [==============================] - 2s 2ms/step - loss: 0.9980 - kullback_leibler_divergence: 0.9980 - acc: 0.5644 - val_loss: 3.4297 - val_kullback_leibler_divergence: 3.4297 - val_acc: 0.1700
Epoch 16/30
900/900 [==============================] - 2s 2ms/step - loss: 0.9551 - kullback_leibler_divergence: 0.9551 - acc: 0.5700 - val_loss: 3.6095 - val_kullback_leibler_divergence: 3.6095 - val_acc: 0.1900
Epoch 17/30
900/900 [==============================] - 2s 2ms/step - loss: 0.9250 - kullback_leibler_divergence: 0.9250 - acc: 0.5833 - val_loss: 3.8133 - val_kullback_leibler_divergence: 3.8133 - val_acc: 0.1800
Epoch 18/30
900/900 [==============================] - 2s 2ms/step - loss: 0.8841 - kullback_leibler_divergence: 0.8841 - acc: 0.5900 - val_loss: 3.9055 - val_kullback_leibler_divergence: 3.9055 - val_acc: 0.1500
Epoch 19/30
900/900 [==============================] - 2s 3ms/step - loss: 0.8589 - kullback_leibler_divergence: 0.8589 - acc: 0.6011 - val_loss: 4.0558 - val_kullback_leibler_divergence: 4.0558 - val_acc: 0.0800
Epoch 20/30
900/900 [==============================] - 2s 3ms/step - loss: 0.8051 - kullback_leibler_divergence: 0.8051 - acc: 0.6267 - val_loss: 4.4488 - val_kullback_leibler_divergence: 4.4488 - val_acc: 0.1300
Epoch 21/30
900/900 [==============================] - 2s 2ms/step - loss: 0.7814 - kullback_leibler_divergence: 0.7814 - acc: 0.6378 - val_loss: 4.3597 - val_kullback_leibler_divergence: 4.3597 - val_acc: 0.1700
Epoch 22/30
900/900 [==============================] - 2s 2ms/step - loss: 0.7740 - kullback_leibler_divergence: 0.7740 - acc: 0.6344 - val_loss: 4.5222 - val_kullback_leibler_divergence: 4.5222 - val_acc: 0.1300
Epoch 23/30
900/900 [==============================] - 2s 2ms/step - loss: 0.7390 - kullback_leibler_divergence: 0.7390 - acc: 0.6689 - val_loss: 4.6568 - val_kullback_leibler_divergence: 4.6568 - val_acc: 0.1900
Epoch 24/30
900/900 [==============================] - 2s 2ms/step - loss: 0.7151 - kullback_leibler_divergence: 0.7151 - acc: 0.6656 - val_loss: 4.8296 - val_kullback_leibler_divergence: 4.8296 - val_acc: 0.1200
Epoch 25/30
900/900 [==============================] - 2s 2ms/step - loss: 0.6827 - kullback_leibler_divergence: 0.6827 - acc: 0.6867 - val_loss: 4.8886 - val_kullback_leibler_divergence: 4.8886 - val_acc: 0.1200
Epoch 26/30
900/900 [==============================] - 2s 2ms/step - loss: 0.6887 - kullback_leibler_divergence: 0.6887 - acc: 0.6589 - val_loss: 4.9520 - val_kullback_leibler_divergence: 4.9520 - val_acc: 0.1800
Epoch 27/30
900/900 [==============================] - 2s 2ms/step - loss: 0.6600 - kullback_leibler_divergence: 0.6600 - acc: 0.6978 - val_loss: 4.9508 - val_kullback_leibler_divergence: 4.9508 - val_acc: 0.1100
Epoch 28/30
900/900 [==============================] - 2s 2ms/step - loss: 0.6369 - kullback_leibler_divergence: 0.6369 - acc: 0.7044 - val_loss: 5.2346 - val_kullback_leibler_divergence: 5.2346 - val_acc: 0.1200
Epoch 29/30
900/900 [==============================] - 2s 2ms/step - loss: 0.6282 - kullback_leibler_divergence: 0.6282 - acc: 0.7156 - val_loss: 5.2194 - val_kullback_leibler_divergence: 5.2194 - val_acc: 0.1300
Epoch 30/30
900/900 [==============================] - 2s 2ms/step - loss: 0.6020 - kullback_leibler_divergence: 0.6020 - acc: 0.7222 - val_loss: 5.0253 - val_kullback_leibler_divergence: 5.0253 - val_acc: 0.1400
train data:
1000/1000 [==============================] - 0s 216us/step
kullback_leibler_divergence :  0.9140322251319886

test data:
10000/10000 [==============================] - 2s 211us/step
acc :  0.2021

test data:
10000/10000 [==============================] - 2s 221us/step
kullback_leibler_divergence :  4.352663523101807
acc :  0.2021
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:56:09.929955 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:56:09.942428 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:56:09.944041 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:56:09.955292 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 17:56:10.006956 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:56:10.012196 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:56:10.101670 4713928128 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:56:10.132221 4713928128 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 17:56:10.303134: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.1939 - kullback_leibler_divergence: 2.1939 - acc: 0.1411 - val_loss: 2.1253 - val_kullback_leibler_divergence: 2.1253 - val_acc: 0.1800
Epoch 2/30
900/900 [==============================] - 1s 836us/step - loss: 2.1099 - kullback_leibler_divergence: 2.1099 - acc: 0.2344 - val_loss: 2.1250 - val_kullback_leibler_divergence: 2.1250 - val_acc: 0.0500
Epoch 3/30
900/900 [==============================] - 1s 822us/step - loss: 2.0636 - kullback_leibler_divergence: 2.0636 - acc: 0.2778 - val_loss: 2.0611 - val_kullback_leibler_divergence: 2.0611 - val_acc: 0.2200
Epoch 4/30
900/900 [==============================] - 1s 838us/step - loss: 2.0052 - kullback_leibler_divergence: 2.0052 - acc: 0.2811 - val_loss: 2.0208 - val_kullback_leibler_divergence: 2.0208 - val_acc: 0.2200
Epoch 5/30
900/900 [==============================] - 1s 843us/step - loss: 1.9269 - kullback_leibler_divergence: 1.9269 - acc: 0.3244 - val_loss: 1.9148 - val_kullback_leibler_divergence: 1.9148 - val_acc: 0.3700
Epoch 6/30
900/900 [==============================] - 1s 832us/step - loss: 1.8691 - kullback_leibler_divergence: 1.8691 - acc: 0.3489 - val_loss: 1.9225 - val_kullback_leibler_divergence: 1.9225 - val_acc: 0.4200
Epoch 7/30
900/900 [==============================] - 1s 828us/step - loss: 1.8002 - kullback_leibler_divergence: 1.8002 - acc: 0.3589 - val_loss: 2.0373 - val_kullback_leibler_divergence: 2.0373 - val_acc: 0.3200
Epoch 8/30
900/900 [==============================] - 1s 1ms/step - loss: 1.7027 - kullback_leibler_divergence: 1.7027 - acc: 0.4311 - val_loss: 1.9900 - val_kullback_leibler_divergence: 1.9900 - val_acc: 0.3500
Epoch 9/30
900/900 [==============================] - 1s 966us/step - loss: 1.6077 - kullback_leibler_divergence: 1.6077 - acc: 0.4467 - val_loss: 2.0827 - val_kullback_leibler_divergence: 2.0827 - val_acc: 0.3300
Epoch 10/30
900/900 [==============================] - 1s 868us/step - loss: 1.5271 - kullback_leibler_divergence: 1.5271 - acc: 0.4722 - val_loss: 2.1283 - val_kullback_leibler_divergence: 2.1283 - val_acc: 0.4000
Epoch 11/30
900/900 [==============================] - 1s 852us/step - loss: 1.4438 - kullback_leibler_divergence: 1.4438 - acc: 0.4889 - val_loss: 2.2878 - val_kullback_leibler_divergence: 2.2878 - val_acc: 0.2900
Epoch 12/30
900/900 [==============================] - 1s 870us/step - loss: 1.3846 - kullback_leibler_divergence: 1.3846 - acc: 0.4944 - val_loss: 2.3431 - val_kullback_leibler_divergence: 2.3431 - val_acc: 0.2300
Epoch 13/30
900/900 [==============================] - 1s 901us/step - loss: 1.3410 - kullback_leibler_divergence: 1.3410 - acc: 0.5133 - val_loss: 2.3021 - val_kullback_leibler_divergence: 2.3021 - val_acc: 0.2900
Epoch 14/30
900/900 [==============================] - 1s 849us/step - loss: 1.2939 - kullback_leibler_divergence: 1.2939 - acc: 0.5022 - val_loss: 2.4914 - val_kullback_leibler_divergence: 2.4914 - val_acc: 0.2600
Epoch 15/30
900/900 [==============================] - 1s 868us/step - loss: 1.2330 - kullback_leibler_divergence: 1.2330 - acc: 0.5400 - val_loss: 2.8933 - val_kullback_leibler_divergence: 2.8933 - val_acc: 0.2000
Epoch 16/30
900/900 [==============================] - 1s 861us/step - loss: 1.1814 - kullback_leibler_divergence: 1.1814 - acc: 0.5567 - val_loss: 2.7553 - val_kullback_leibler_divergence: 2.7553 - val_acc: 0.2100
Epoch 17/30
900/900 [==============================] - 1s 880us/step - loss: 1.1611 - kullback_leibler_divergence: 1.1611 - acc: 0.5489 - val_loss: 2.7789 - val_kullback_leibler_divergence: 2.7789 - val_acc: 0.1700
Epoch 18/30
900/900 [==============================] - 1s 881us/step - loss: 1.1140 - kullback_leibler_divergence: 1.1140 - acc: 0.5367 - val_loss: 2.8659 - val_kullback_leibler_divergence: 2.8659 - val_acc: 0.1800
Epoch 19/30
900/900 [==============================] - 1s 862us/step - loss: 1.0917 - kullback_leibler_divergence: 1.0917 - acc: 0.5656 - val_loss: 3.0162 - val_kullback_leibler_divergence: 3.0162 - val_acc: 0.1300
Epoch 20/30
900/900 [==============================] - 1s 851us/step - loss: 1.0240 - kullback_leibler_divergence: 1.0240 - acc: 0.5611 - val_loss: 3.1717 - val_kullback_leibler_divergence: 3.1717 - val_acc: 0.1400
Epoch 21/30
900/900 [==============================] - 1s 847us/step - loss: 0.9705 - kullback_leibler_divergence: 0.9705 - acc: 0.6011 - val_loss: 3.3437 - val_kullback_leibler_divergence: 3.3437 - val_acc: 0.1600
Epoch 22/30
900/900 [==============================] - 1s 882us/step - loss: 0.9418 - kullback_leibler_divergence: 0.9418 - acc: 0.5944 - val_loss: 3.0550 - val_kullback_leibler_divergence: 3.0550 - val_acc: 0.1500
Epoch 23/30
900/900 [==============================] - 1s 879us/step - loss: 0.9033 - kullback_leibler_divergence: 0.9033 - acc: 0.6056 - val_loss: 3.3679 - val_kullback_leibler_divergence: 3.3679 - val_acc: 0.1600
Epoch 24/30
900/900 [==============================] - 1s 850us/step - loss: 0.8803 - kullback_leibler_divergence: 0.8803 - acc: 0.6144 - val_loss: 3.4895 - val_kullback_leibler_divergence: 3.4895 - val_acc: 0.1400
Epoch 25/30
900/900 [==============================] - 1s 862us/step - loss: 0.8906 - kullback_leibler_divergence: 0.8906 - acc: 0.5844 - val_loss: 3.6068 - val_kullback_leibler_divergence: 3.6068 - val_acc: 0.1300
Epoch 26/30
900/900 [==============================] - 1s 867us/step - loss: 0.8742 - kullback_leibler_divergence: 0.8742 - acc: 0.6311 - val_loss: 3.5374 - val_kullback_leibler_divergence: 3.5374 - val_acc: 0.1000
Epoch 27/30
900/900 [==============================] - 1s 877us/step - loss: 0.8407 - kullback_leibler_divergence: 0.8407 - acc: 0.6322 - val_loss: 3.8253 - val_kullback_leibler_divergence: 3.8253 - val_acc: 0.1800
Epoch 28/30
900/900 [==============================] - 1s 867us/step - loss: 0.8199 - kullback_leibler_divergence: 0.8199 - acc: 0.6389 - val_loss: 3.9818 - val_kullback_leibler_divergence: 3.9818 - val_acc: 0.1300
Epoch 29/30
900/900 [==============================] - 1s 850us/step - loss: 0.7830 - kullback_leibler_divergence: 0.7830 - acc: 0.6422 - val_loss: 4.0559 - val_kullback_leibler_divergence: 4.0559 - val_acc: 0.1400
Epoch 30/30
900/900 [==============================] - 1s 872us/step - loss: 0.7684 - kullback_leibler_divergence: 0.7684 - acc: 0.6378 - val_loss: 3.8082 - val_kullback_leibler_divergence: 3.8082 - val_acc: 0.1200
train data:
1000/1000 [==============================] - 0s 233us/step
kullback_leibler_divergence :  1.027858052253723

test data:
10000/10000 [==============================] - 2s 231us/step
acc :  0.2216

test data:
10000/10000 [==============================] - 2s 230us/step
kullback_leibler_divergence :  3.4813865127563477
acc :  0.2216
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:58:13.725975 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:58:13.738257 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:58:13.739941 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:58:13.751313 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 17:58:13.806073 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:58:13.811470 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:58:13.901837 4611638720 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:58:13.932638 4611638720 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/30
2019-06-26 17:58:14.104255: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.1544 - kullback_leibler_divergence: 2.1544 - acc: 0.1833 - val_loss: 2.1143 - val_kullback_leibler_divergence: 2.1143 - val_acc: 0.1600
Epoch 2/30
900/900 [==============================] - 1s 850us/step - loss: 2.0612 - kullback_leibler_divergence: 2.0612 - acc: 0.2578 - val_loss: 2.0042 - val_kullback_leibler_divergence: 2.0042 - val_acc: 0.2900
Epoch 3/30
900/900 [==============================] - 1s 823us/step - loss: 1.9738 - kullback_leibler_divergence: 1.9738 - acc: 0.3022 - val_loss: 1.9592 - val_kullback_leibler_divergence: 1.9592 - val_acc: 0.3600
Epoch 4/30
900/900 [==============================] - 1s 865us/step - loss: 1.9090 - kullback_leibler_divergence: 1.9090 - acc: 0.3389 - val_loss: 2.0496 - val_kullback_leibler_divergence: 2.0496 - val_acc: 0.2200
Epoch 5/30
900/900 [==============================] - 1s 864us/step - loss: 1.7921 - kullback_leibler_divergence: 1.7921 - acc: 0.3889 - val_loss: 2.0655 - val_kullback_leibler_divergence: 2.0655 - val_acc: 0.2300
Epoch 6/30
900/900 [==============================] - 1s 876us/step - loss: 1.7274 - kullback_leibler_divergence: 1.7274 - acc: 0.3967 - val_loss: 2.0470 - val_kullback_leibler_divergence: 2.0470 - val_acc: 0.2300
Epoch 7/30
900/900 [==============================] - 1s 883us/step - loss: 1.6566 - kullback_leibler_divergence: 1.6566 - acc: 0.4311 - val_loss: 2.2123 - val_kullback_leibler_divergence: 2.2123 - val_acc: 0.2700
Epoch 8/30
900/900 [==============================] - 1s 839us/step - loss: 1.6135 - kullback_leibler_divergence: 1.6135 - acc: 0.4511 - val_loss: 2.1017 - val_kullback_leibler_divergence: 2.1017 - val_acc: 0.2800
Epoch 9/30
900/900 [==============================] - 1s 837us/step - loss: 1.5331 - kullback_leibler_divergence: 1.5331 - acc: 0.4667 - val_loss: 2.3116 - val_kullback_leibler_divergence: 2.3116 - val_acc: 0.2100
Epoch 10/30
900/900 [==============================] - 1s 848us/step - loss: 1.4712 - kullback_leibler_divergence: 1.4712 - acc: 0.4622 - val_loss: 2.2177 - val_kullback_leibler_divergence: 2.2177 - val_acc: 0.3200
Epoch 11/30
900/900 [==============================] - 1s 862us/step - loss: 1.3753 - kullback_leibler_divergence: 1.3753 - acc: 0.5067 - val_loss: 2.4103 - val_kullback_leibler_divergence: 2.4103 - val_acc: 0.2000
Epoch 12/30
900/900 [==============================] - 1s 849us/step - loss: 1.3424 - kullback_leibler_divergence: 1.3424 - acc: 0.5122 - val_loss: 2.4141 - val_kullback_leibler_divergence: 2.4141 - val_acc: 0.2700
Epoch 13/30
900/900 [==============================] - 1s 869us/step - loss: 1.2609 - kullback_leibler_divergence: 1.2609 - acc: 0.5267 - val_loss: 2.7796 - val_kullback_leibler_divergence: 2.7796 - val_acc: 0.1400
Epoch 14/30
900/900 [==============================] - 1s 857us/step - loss: 1.2158 - kullback_leibler_divergence: 1.2158 - acc: 0.5333 - val_loss: 2.6726 - val_kullback_leibler_divergence: 2.6726 - val_acc: 0.2100
Epoch 15/30
900/900 [==============================] - 1s 842us/step - loss: 1.2028 - kullback_leibler_divergence: 1.2028 - acc: 0.5389 - val_loss: 2.7512 - val_kullback_leibler_divergence: 2.7512 - val_acc: 0.1800
Epoch 16/30
900/900 [==============================] - 1s 860us/step - loss: 1.1606 - kullback_leibler_divergence: 1.1606 - acc: 0.5433 - val_loss: 2.7367 - val_kullback_leibler_divergence: 2.7367 - val_acc: 0.1700
Epoch 17/30
900/900 [==============================] - 1s 855us/step - loss: 1.0970 - kullback_leibler_divergence: 1.0970 - acc: 0.5556 - val_loss: 2.6991 - val_kullback_leibler_divergence: 2.6991 - val_acc: 0.2200
Epoch 18/30
900/900 [==============================] - 1s 849us/step - loss: 1.0260 - kullback_leibler_divergence: 1.0260 - acc: 0.5722 - val_loss: 2.9980 - val_kullback_leibler_divergence: 2.9980 - val_acc: 0.2200
Epoch 19/30
900/900 [==============================] - 1s 855us/step - loss: 1.0437 - kullback_leibler_divergence: 1.0437 - acc: 0.5544 - val_loss: 2.9709 - val_kullback_leibler_divergence: 2.9709 - val_acc: 0.2200
Epoch 20/30
900/900 [==============================] - 1s 975us/step - loss: 1.0214 - kullback_leibler_divergence: 1.0214 - acc: 0.5711 - val_loss: 2.8698 - val_kullback_leibler_divergence: 2.8698 - val_acc: 0.2000
Epoch 21/30
900/900 [==============================] - 1s 846us/step - loss: 0.9788 - kullback_leibler_divergence: 0.9788 - acc: 0.5700 - val_loss: 2.9476 - val_kullback_leibler_divergence: 2.9476 - val_acc: 0.2100
Epoch 22/30
900/900 [==============================] - 1s 869us/step - loss: 0.9325 - kullback_leibler_divergence: 0.9325 - acc: 0.6144 - val_loss: 3.3594 - val_kullback_leibler_divergence: 3.3594 - val_acc: 0.2000
Epoch 23/30
900/900 [==============================] - 1s 857us/step - loss: 0.9116 - kullback_leibler_divergence: 0.9116 - acc: 0.5956 - val_loss: 3.3525 - val_kullback_leibler_divergence: 3.3525 - val_acc: 0.1400
Epoch 24/30
900/900 [==============================] - 1s 843us/step - loss: 0.9255 - kullback_leibler_divergence: 0.9255 - acc: 0.5911 - val_loss: 3.4784 - val_kullback_leibler_divergence: 3.4784 - val_acc: 0.1500
Epoch 25/30
900/900 [==============================] - 1s 858us/step - loss: 0.8903 - kullback_leibler_divergence: 0.8903 - acc: 0.6100 - val_loss: 3.5760 - val_kullback_leibler_divergence: 3.5760 - val_acc: 0.1600
Epoch 26/30
900/900 [==============================] - 1s 864us/step - loss: 0.9171 - kullback_leibler_divergence: 0.9171 - acc: 0.5933 - val_loss: 3.9987 - val_kullback_leibler_divergence: 3.9987 - val_acc: 0.1400
Epoch 27/30
900/900 [==============================] - 1s 873us/step - loss: 0.9284 - kullback_leibler_divergence: 0.9284 - acc: 0.5833 - val_loss: 3.2226 - val_kullback_leibler_divergence: 3.2226 - val_acc: 0.1800
Epoch 28/30
900/900 [==============================] - 1s 861us/step - loss: 0.8788 - kullback_leibler_divergence: 0.8788 - acc: 0.6033 - val_loss: 3.5533 - val_kullback_leibler_divergence: 3.5533 - val_acc: 0.1400
Epoch 29/30
900/900 [==============================] - 1s 880us/step - loss: 0.8168 - kullback_leibler_divergence: 0.8168 - acc: 0.6300 - val_loss: 4.1496 - val_kullback_leibler_divergence: 4.1496 - val_acc: 0.1200
Epoch 30/30
900/900 [==============================] - 1s 902us/step - loss: 0.8203 - kullback_leibler_divergence: 0.8203 - acc: 0.6233 - val_loss: 3.9533 - val_kullback_leibler_divergence: 3.9533 - val_acc: 0.1600
train data:
1000/1000 [==============================] - 0s 238us/step
kullback_leibler_divergence :  1.055892177581787

acc :  0.633

test data:
10000/10000 [==============================] - 2s 245us/step
kullback_leibler_divergence :  3.5776813610076905
acc :  0.2126
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 17:59:15.881288 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 17:59:15.895550 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 17:59:15.897927 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 17:59:15.912869 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 17:59:15.965243 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 17:59:15.971027 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 17:59:16.061164 4610512320 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 17:59:16.092705 4610512320 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 17:59:16.272447: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.1632 - kullback_leibler_divergence: 2.1632 - acc: 0.2178 - val_loss: 2.1330 - val_kullback_leibler_divergence: 2.1330 - val_acc: 0.2400
Epoch 2/50
900/900 [==============================] - 1s 846us/step - loss: 2.0875 - kullback_leibler_divergence: 2.0875 - acc: 0.2411 - val_loss: 2.0244 - val_kullback_leibler_divergence: 2.0244 - val_acc: 0.2400
Epoch 3/50
900/900 [==============================] - 1s 877us/step - loss: 2.0138 - kullback_leibler_divergence: 2.0138 - acc: 0.2678 - val_loss: 2.0027 - val_kullback_leibler_divergence: 2.0027 - val_acc: 0.2800
Epoch 4/50
900/900 [==============================] - 1s 903us/step - loss: 1.9514 - kullback_leibler_divergence: 1.9514 - acc: 0.3244 - val_loss: 1.9611 - val_kullback_leibler_divergence: 1.9611 - val_acc: 0.2900
Epoch 5/50
900/900 [==============================] - 1s 854us/step - loss: 1.8698 - kullback_leibler_divergence: 1.8698 - acc: 0.3578 - val_loss: 1.9478 - val_kullback_leibler_divergence: 1.9478 - val_acc: 0.2800
Epoch 6/50
900/900 [==============================] - 1s 859us/step - loss: 1.7968 - kullback_leibler_divergence: 1.7968 - acc: 0.3956 - val_loss: 2.0758 - val_kullback_leibler_divergence: 2.0758 - val_acc: 0.2700
Epoch 7/50
900/900 [==============================] - 1s 858us/step - loss: 1.7444 - kullback_leibler_divergence: 1.7444 - acc: 0.3967 - val_loss: 2.1850 - val_kullback_leibler_divergence: 2.1850 - val_acc: 0.2100
Epoch 8/50
900/900 [==============================] - 1s 884us/step - loss: 1.6610 - kullback_leibler_divergence: 1.6610 - acc: 0.4356 - val_loss: 2.2546 - val_kullback_leibler_divergence: 2.2546 - val_acc: 0.1400
Epoch 9/50
900/900 [==============================] - 1s 833us/step - loss: 1.6099 - kullback_leibler_divergence: 1.6099 - acc: 0.4467 - val_loss: 2.0520 - val_kullback_leibler_divergence: 2.0520 - val_acc: 0.3600
Epoch 10/50
900/900 [==============================] - 1s 885us/step - loss: 1.4997 - kullback_leibler_divergence: 1.4997 - acc: 0.4844 - val_loss: 1.9833 - val_kullback_leibler_divergence: 1.9833 - val_acc: 0.3900
Epoch 11/50
900/900 [==============================] - 1s 874us/step - loss: 1.4502 - kullback_leibler_divergence: 1.4502 - acc: 0.4956 - val_loss: 2.1113 - val_kullback_leibler_divergence: 2.1113 - val_acc: 0.2900
Epoch 12/50
900/900 [==============================] - 1s 829us/step - loss: 1.3960 - kullback_leibler_divergence: 1.3960 - acc: 0.4878 - val_loss: 2.1425 - val_kullback_leibler_divergence: 2.1425 - val_acc: 0.2800
Epoch 13/50
900/900 [==============================] - 1s 853us/step - loss: 1.3286 - kullback_leibler_divergence: 1.3286 - acc: 0.5078 - val_loss: 2.3939 - val_kullback_leibler_divergence: 2.3939 - val_acc: 0.3200
Epoch 14/50
900/900 [==============================] - 1s 875us/step - loss: 1.2623 - kullback_leibler_divergence: 1.2623 - acc: 0.5244 - val_loss: 2.6088 - val_kullback_leibler_divergence: 2.6088 - val_acc: 0.2500
Epoch 15/50
900/900 [==============================] - 1s 865us/step - loss: 1.2553 - kullback_leibler_divergence: 1.2553 - acc: 0.5267 - val_loss: 2.5599 - val_kullback_leibler_divergence: 2.5599 - val_acc: 0.2600
Epoch 16/50
900/900 [==============================] - 1s 837us/step - loss: 1.1787 - kullback_leibler_divergence: 1.1787 - acc: 0.5367 - val_loss: 2.7876 - val_kullback_leibler_divergence: 2.7876 - val_acc: 0.2500
Epoch 17/50
900/900 [==============================] - 1s 861us/step - loss: 1.1179 - kullback_leibler_divergence: 1.1179 - acc: 0.5522 - val_loss: 2.7955 - val_kullback_leibler_divergence: 2.7955 - val_acc: 0.2500
Epoch 18/50
900/900 [==============================] - 1s 1ms/step - loss: 1.0564 - kullback_leibler_divergence: 1.0564 - acc: 0.5611 - val_loss: 2.8543 - val_kullback_leibler_divergence: 2.8543 - val_acc: 0.1900
Epoch 19/50
900/900 [==============================] - 1s 881us/step - loss: 1.0469 - kullback_leibler_divergence: 1.0469 - acc: 0.5711 - val_loss: 2.8222 - val_kullback_leibler_divergence: 2.8222 - val_acc: 0.1600
Epoch 20/50
900/900 [==============================] - 1s 866us/step - loss: 1.0412 - kullback_leibler_divergence: 1.0412 - acc: 0.5589 - val_loss: 2.8937 - val_kullback_leibler_divergence: 2.8937 - val_acc: 0.1700
Epoch 21/50
900/900 [==============================] - 1s 868us/step - loss: 0.9891 - kullback_leibler_divergence: 0.9891 - acc: 0.5667 - val_loss: 2.9155 - val_kullback_leibler_divergence: 2.9155 - val_acc: 0.2000
Epoch 22/50
900/900 [==============================] - 1s 847us/step - loss: 0.9713 - kullback_leibler_divergence: 0.9713 - acc: 0.5844 - val_loss: 2.9910 - val_kullback_leibler_divergence: 2.9910 - val_acc: 0.1600
Epoch 23/50
900/900 [==============================] - 1s 865us/step - loss: 0.9632 - kullback_leibler_divergence: 0.9632 - acc: 0.5833 - val_loss: 3.3385 - val_kullback_leibler_divergence: 3.3385 - val_acc: 0.1100
Epoch 24/50
900/900 [==============================] - 1s 847us/step - loss: 0.8997 - kullback_leibler_divergence: 0.8997 - acc: 0.5856 - val_loss: 3.2351 - val_kullback_leibler_divergence: 3.2351 - val_acc: 0.2100
Epoch 25/50
900/900 [==============================] - 1s 837us/step - loss: 0.8835 - kullback_leibler_divergence: 0.8835 - acc: 0.6000 - val_loss: 3.4017 - val_kullback_leibler_divergence: 3.4017 - val_acc: 0.1900
Epoch 26/50
900/900 [==============================] - 1s 869us/step - loss: 0.8903 - kullback_leibler_divergence: 0.8903 - acc: 0.6111 - val_loss: 4.0021 - val_kullback_leibler_divergence: 4.0021 - val_acc: 0.1400
Epoch 27/50
900/900 [==============================] - 1s 853us/step - loss: 0.9166 - kullback_leibler_divergence: 0.9166 - acc: 0.5944 - val_loss: 3.5798 - val_kullback_leibler_divergence: 3.5798 - val_acc: 0.1600
Epoch 28/50
900/900 [==============================] - 1s 862us/step - loss: 0.8952 - kullback_leibler_divergence: 0.8952 - acc: 0.5844 - val_loss: 3.6100 - val_kullback_leibler_divergence: 3.6100 - val_acc: 0.1500
Epoch 29/50
900/900 [==============================] - 1s 849us/step - loss: 0.8422 - kullback_leibler_divergence: 0.8422 - acc: 0.6033 - val_loss: 3.4254 - val_kullback_leibler_divergence: 3.4254 - val_acc: 0.1600
Epoch 30/50
900/900 [==============================] - 1s 858us/step - loss: 0.8303 - kullback_leibler_divergence: 0.8303 - acc: 0.6289 - val_loss: 3.5638 - val_kullback_leibler_divergence: 3.5638 - val_acc: 0.1600
Epoch 31/50
900/900 [==============================] - 1s 846us/step - loss: 0.8135 - kullback_leibler_divergence: 0.8135 - acc: 0.6322 - val_loss: 3.8393 - val_kullback_leibler_divergence: 3.8393 - val_acc: 0.1300
Epoch 32/50
900/900 [==============================] - 1s 863us/step - loss: 0.7900 - kullback_leibler_divergence: 0.7900 - acc: 0.6222 - val_loss: 4.1667 - val_kullback_leibler_divergence: 4.1667 - val_acc: 0.1400
Epoch 33/50
900/900 [==============================] - 1s 857us/step - loss: 0.7779 - kullback_leibler_divergence: 0.7779 - acc: 0.6389 - val_loss: 3.9619 - val_kullback_leibler_divergence: 3.9619 - val_acc: 0.1700
Epoch 34/50
900/900 [==============================] - 1s 857us/step - loss: 0.7658 - kullback_leibler_divergence: 0.7658 - acc: 0.6378 - val_loss: 3.9904 - val_kullback_leibler_divergence: 3.9904 - val_acc: 0.1400
Epoch 35/50
900/900 [==============================] - 1s 829us/step - loss: 0.7799 - kullback_leibler_divergence: 0.7799 - acc: 0.6144 - val_loss: 3.9117 - val_kullback_leibler_divergence: 3.9117 - val_acc: 0.1600
Epoch 36/50
900/900 [==============================] - 1s 954us/step - loss: 0.7443 - kullback_leibler_divergence: 0.7443 - acc: 0.6556 - val_loss: 4.3369 - val_kullback_leibler_divergence: 4.3369 - val_acc: 0.1200
Epoch 37/50
900/900 [==============================] - 1s 866us/step - loss: 0.6935 - kullback_leibler_divergence: 0.6935 - acc: 0.6767 - val_loss: 4.4240 - val_kullback_leibler_divergence: 4.4240 - val_acc: 0.1600
Epoch 38/50
900/900 [==============================] - 1s 845us/step - loss: 0.7146 - kullback_leibler_divergence: 0.7146 - acc: 0.6589 - val_loss: 4.2946 - val_kullback_leibler_divergence: 4.2946 - val_acc: 0.1400
Epoch 39/50
900/900 [==============================] - 1s 849us/step - loss: 0.7331 - kullback_leibler_divergence: 0.7331 - acc: 0.6511 - val_loss: 4.3963 - val_kullback_leibler_divergence: 4.3963 - val_acc: 0.1400
Epoch 40/50
900/900 [==============================] - 1s 864us/step - loss: 0.6962 - kullback_leibler_divergence: 0.6962 - acc: 0.6833 - val_loss: 4.5609 - val_kullback_leibler_divergence: 4.5609 - val_acc: 0.1200
Epoch 41/50
900/900 [==============================] - 1s 850us/step - loss: 0.7057 - kullback_leibler_divergence: 0.7057 - acc: 0.6489 - val_loss: 4.3943 - val_kullback_leibler_divergence: 4.3943 - val_acc: 0.1300
Epoch 42/50
900/900 [==============================] - 1s 871us/step - loss: 0.7072 - kullback_leibler_divergence: 0.7072 - acc: 0.6533 - val_loss: 4.3320 - val_kullback_leibler_divergence: 4.3320 - val_acc: 0.1200
Epoch 43/50
900/900 [==============================] - 1s 859us/step - loss: 0.7059 - kullback_leibler_divergence: 0.7059 - acc: 0.6678 - val_loss: 4.2434 - val_kullback_leibler_divergence: 4.2434 - val_acc: 0.1500
Epoch 44/50
900/900 [==============================] - 1s 986us/step - loss: 0.6926 - kullback_leibler_divergence: 0.6926 - acc: 0.6678 - val_loss: 4.3375 - val_kullback_leibler_divergence: 4.3375 - val_acc: 0.1600
Epoch 45/50
900/900 [==============================] - 1s 855us/step - loss: 0.6865 - kullback_leibler_divergence: 0.6865 - acc: 0.6811 - val_loss: 4.3423 - val_kullback_leibler_divergence: 4.3423 - val_acc: 0.1600
Epoch 46/50
900/900 [==============================] - 1s 878us/step - loss: 0.6792 - kullback_leibler_divergence: 0.6792 - acc: 0.6744 - val_loss: 4.3662 - val_kullback_leibler_divergence: 4.3662 - val_acc: 0.1700
Epoch 47/50
900/900 [==============================] - 1s 868us/step - loss: 0.6580 - kullback_leibler_divergence: 0.6580 - acc: 0.6844 - val_loss: 4.6714 - val_kullback_leibler_divergence: 4.6714 - val_acc: 0.1200
Epoch 48/50
900/900 [==============================] - 1s 853us/step - loss: 0.6365 - kullback_leibler_divergence: 0.6365 - acc: 0.6922 - val_loss: 4.9580 - val_kullback_leibler_divergence: 4.9580 - val_acc: 0.1400
Epoch 49/50
900/900 [==============================] - 1s 855us/step - loss: 0.6514 - kullback_leibler_divergence: 0.6514 - acc: 0.7000 - val_loss: 4.5218 - val_kullback_leibler_divergence: 4.5218 - val_acc: 0.1200
Epoch 50/50
900/900 [==============================] - 1s 879us/step - loss: 0.6424 - kullback_leibler_divergence: 0.6424 - acc: 0.6933 - val_loss: 4.5621 - val_kullback_leibler_divergence: 4.5621 - val_acc: 0.1500
train data:
1000/1000 [==============================] - 0s 233us/step
kullback_leibler_divergence :  0.9996074695587158

acc :  0.665

test data:
10000/10000 [==============================] - 2s 231us/step
kullback_leibler_divergence :  4.10100675125122
acc :  0.2101
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 64, in <module>
    X_train.append(cv2.addWeighted(X_train[i],0.3,sub_X_train2[i],0.7,0))#X_train[i] = cv2.addWeighted(X_train[i],0.3,sub_X_train2[i],0.7,0)
AttributeError: 'numpy.ndarray' object has no attribute 'append'
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
^CTraceback (most recent call last):
  File "imageBC.py", line 12, in <module>
    import data
  File "/Users/shoichi/Desktop/research_git/train1000-master/data.py", line 4, in <module>
    from keras import backend as K
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/__init__.py", line 3, in <module>
    from . import utils
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/utils/__init__.py", line 6, in <module>
    from . import conv_utils
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/utils/conv_utils.py", line 9, in <module>
    from .. import backend as K
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/__init__.py", line 89, in <module>
    from .tensorflow_backend import *
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py", line 5, in <module>
    import tensorflow as tf
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/__init__.py", line 28, in <module>
    from tensorflow.python import pywrap_tensorflow  # pylint: disable=unused-import
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/__init__.py", line 73, in <module>
    from tensorflow.python.ops.standard_ops import *
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/standard_ops.py", line 25, in <module>
    from tensorflow.python import autograph
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/autograph/__init__.py", line 35, in <module>
    from tensorflow.python.autograph import operators
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/autograph/operators/__init__.py", line 40, in <module>
    from tensorflow.python.autograph.operators.control_flow import for_stmt
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/autograph/operators/control_flow.py", line 24, in <module>
    from tensorflow.python.data.experimental.ops import scan_ops
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/data/__init__.py", line 25, in <module>
    from tensorflow.python.data import experimental
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/data/experimental/__init__.py", line 90, in <module>
    from tensorflow.python.data.experimental.ops.batching import dense_to_sparse_batch
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/data/experimental/ops/batching.py", line 20, in <module>
    from tensorflow.python.data.ops import dataset_ops
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/data/ops/dataset_ops.py", line 35, in <module>
    from tensorflow.python.data.experimental.ops import stats_options
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/data/experimental/ops/stats_options.py", line 22, in <module>
    from tensorflow.python.data.experimental.ops import stats_aggregator
  File "/Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/data/experimental/ops/stats_aggregator.py", line 22, in <module>
    from tensorflow.python.ops import gen_experimental_dataset_ops as ged_ops
  File "<frozen importlib._bootstrap>", line 983, in _find_and_load
  File "<frozen importlib._bootstrap>", line 967, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 677, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 724, in exec_module
  File "<frozen importlib._bootstrap_external>", line 818, in get_code
  File "<frozen importlib._bootstrap_external>", line 917, in get_data
KeyboardInterrupt
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
Traceback (most recent call last):
  File "imageBC.py", line 64, in <module>
    X_train[i].append(cv2.addWeighted(X_train[i],0.3,sub_X_train2[i],0.7,0))#X_train[i] = cv2.addWeighted(X_train[i],0.3,sub_X_train2[i],0.7,0)
AttributeError: 'numpy.ndarray' object has no attribute 'append'
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 65
    np.append(X_train,cv2.addWeighted(X_train[i+500],0.7,sub_X_train1[i],0.3,0))
                                                                               ^
TabError: inconsistent use of tabs and spaces in indentation
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 18:10:12.783211 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 18:10:12.797708 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 18:10:12.800881 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 18:10:12.816033 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 18:10:12.871238 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 18:10:12.876435 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 18:10:12.967165 4643505600 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 18:10:12.999176 4643505600 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 18:10:13.187333: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.1525 - kullback_leibler_divergence: 2.1525 - acc: 0.2011 - val_loss: 2.0802 - val_kullback_leibler_divergence: 2.0802 - val_acc: 0.1700
Epoch 2/50
900/900 [==============================] - 1s 799us/step - loss: 1.8989 - kullback_leibler_divergence: 1.8989 - acc: 0.3322 - val_loss: 1.8478 - val_kullback_leibler_divergence: 1.8478 - val_acc: 0.2400
Epoch 3/50
900/900 [==============================] - 1s 810us/step - loss: 1.6966 - kullback_leibler_divergence: 1.6966 - acc: 0.4156 - val_loss: 1.7575 - val_kullback_leibler_divergence: 1.7575 - val_acc: 0.3800
Epoch 4/50
900/900 [==============================] - 1s 833us/step - loss: 1.4984 - kullback_leibler_divergence: 1.4984 - acc: 0.4989 - val_loss: 1.4796 - val_kullback_leibler_divergence: 1.4796 - val_acc: 0.5000
Epoch 5/50
900/900 [==============================] - 1s 813us/step - loss: 1.3625 - kullback_leibler_divergence: 1.3625 - acc: 0.5400 - val_loss: 1.5614 - val_kullback_leibler_divergence: 1.5614 - val_acc: 0.4300
Epoch 6/50
900/900 [==============================] - 1s 830us/step - loss: 1.1946 - kullback_leibler_divergence: 1.1946 - acc: 0.6078 - val_loss: 1.6137 - val_kullback_leibler_divergence: 1.6137 - val_acc: 0.3400
Epoch 7/50
900/900 [==============================] - 1s 986us/step - loss: 1.1067 - kullback_leibler_divergence: 1.1067 - acc: 0.6333 - val_loss: 1.6790 - val_kullback_leibler_divergence: 1.6790 - val_acc: 0.3800
Epoch 8/50
900/900 [==============================] - 1s 1ms/step - loss: 0.9666 - kullback_leibler_divergence: 0.9666 - acc: 0.6733 - val_loss: 1.6456 - val_kullback_leibler_divergence: 1.6456 - val_acc: 0.3900
Epoch 9/50
900/900 [==============================] - 1s 856us/step - loss: 0.8533 - kullback_leibler_divergence: 0.8533 - acc: 0.7333 - val_loss: 1.5339 - val_kullback_leibler_divergence: 1.5339 - val_acc: 0.4800
Epoch 10/50
900/900 [==============================] - 1s 829us/step - loss: 0.7261 - kullback_leibler_divergence: 0.7261 - acc: 0.7889 - val_loss: 1.5477 - val_kullback_leibler_divergence: 1.5477 - val_acc: 0.4100
Epoch 11/50
900/900 [==============================] - 1s 858us/step - loss: 0.6303 - kullback_leibler_divergence: 0.6303 - acc: 0.8144 - val_loss: 1.5795 - val_kullback_leibler_divergence: 1.5795 - val_acc: 0.4800
Epoch 12/50
900/900 [==============================] - 1s 853us/step - loss: 0.5175 - kullback_leibler_divergence: 0.5175 - acc: 0.8611 - val_loss: 1.6795 - val_kullback_leibler_divergence: 1.6795 - val_acc: 0.4100
Epoch 13/50
900/900 [==============================] - 1s 817us/step - loss: 0.4617 - kullback_leibler_divergence: 0.4617 - acc: 0.8744 - val_loss: 1.5424 - val_kullback_leibler_divergence: 1.5424 - val_acc: 0.4700
Epoch 14/50
900/900 [==============================] - 1s 847us/step - loss: 0.4203 - kullback_leibler_divergence: 0.4203 - acc: 0.8700 - val_loss: 1.6929 - val_kullback_leibler_divergence: 1.6929 - val_acc: 0.5300
Epoch 15/50
900/900 [==============================] - 1s 867us/step - loss: 0.3786 - kullback_leibler_divergence: 0.3786 - acc: 0.8922 - val_loss: 1.8106 - val_kullback_leibler_divergence: 1.8106 - val_acc: 0.4500
Epoch 16/50
900/900 [==============================] - 1s 837us/step - loss: 0.2902 - kullback_leibler_divergence: 0.2902 - acc: 0.9411 - val_loss: 1.9663 - val_kullback_leibler_divergence: 1.9663 - val_acc: 0.4300
Epoch 17/50
900/900 [==============================] - 1s 897us/step - loss: 0.2370 - kullback_leibler_divergence: 0.2370 - acc: 0.9478 - val_loss: 1.9043 - val_kullback_leibler_divergence: 1.9043 - val_acc: 0.3800
Epoch 18/50
900/900 [==============================] - 1s 855us/step - loss: 0.1947 - kullback_leibler_divergence: 0.1947 - acc: 0.9589 - val_loss: 1.9855 - val_kullback_leibler_divergence: 1.9855 - val_acc: 0.4300
Epoch 19/50
900/900 [==============================] - 1s 867us/step - loss: 0.1729 - kullback_leibler_divergence: 0.1729 - acc: 0.9678 - val_loss: 1.8943 - val_kullback_leibler_divergence: 1.8943 - val_acc: 0.4900
Epoch 20/50
900/900 [==============================] - 1s 895us/step - loss: 0.1247 - kullback_leibler_divergence: 0.1247 - acc: 0.9833 - val_loss: 1.7872 - val_kullback_leibler_divergence: 1.7872 - val_acc: 0.4900
Epoch 21/50
900/900 [==============================] - 1s 943us/step - loss: 0.0954 - kullback_leibler_divergence: 0.0954 - acc: 0.9911 - val_loss: 1.7647 - val_kullback_leibler_divergence: 1.7647 - val_acc: 0.5200
Epoch 22/50
900/900 [==============================] - 1s 869us/step - loss: 0.0771 - kullback_leibler_divergence: 0.0771 - acc: 0.9933 - val_loss: 2.0275 - val_kullback_leibler_divergence: 2.0275 - val_acc: 0.5000
Epoch 23/50
900/900 [==============================] - 1s 867us/step - loss: 0.0601 - kullback_leibler_divergence: 0.0601 - acc: 0.9967 - val_loss: 2.0249 - val_kullback_leibler_divergence: 2.0249 - val_acc: 0.4800
Epoch 24/50
900/900 [==============================] - 1s 839us/step - loss: 0.0487 - kullback_leibler_divergence: 0.0487 - acc: 0.9978 - val_loss: 2.0564 - val_kullback_leibler_divergence: 2.0564 - val_acc: 0.5200
Epoch 25/50
900/900 [==============================] - 1s 877us/step - loss: 0.0406 - kullback_leibler_divergence: 0.0406 - acc: 0.9978 - val_loss: 2.0768 - val_kullback_leibler_divergence: 2.0768 - val_acc: 0.4900
Epoch 26/50
900/900 [==============================] - 1s 885us/step - loss: 0.0315 - kullback_leibler_divergence: 0.0315 - acc: 1.0000 - val_loss: 2.3218 - val_kullback_leibler_divergence: 2.3218 - val_acc: 0.4500
Epoch 27/50
900/900 [==============================] - 1s 871us/step - loss: 0.0275 - kullback_leibler_divergence: 0.0275 - acc: 1.0000 - val_loss: 2.2316 - val_kullback_leibler_divergence: 2.2316 - val_acc: 0.5000
Epoch 28/50
900/900 [==============================] - 1s 877us/step - loss: 0.0238 - kullback_leibler_divergence: 0.0238 - acc: 1.0000 - val_loss: 2.3806 - val_kullback_leibler_divergence: 2.3806 - val_acc: 0.5000
Epoch 29/50
900/900 [==============================] - 1s 871us/step - loss: 0.0194 - kullback_leibler_divergence: 0.0194 - acc: 1.0000 - val_loss: 2.5052 - val_kullback_leibler_divergence: 2.5052 - val_acc: 0.4700
Epoch 30/50
900/900 [==============================] - 1s 857us/step - loss: 0.0171 - kullback_leibler_divergence: 0.0171 - acc: 1.0000 - val_loss: 2.3770 - val_kullback_leibler_divergence: 2.3770 - val_acc: 0.5000
Epoch 31/50
900/900 [==============================] - 1s 849us/step - loss: 0.0153 - kullback_leibler_divergence: 0.0153 - acc: 1.0000 - val_loss: 2.5060 - val_kullback_leibler_divergence: 2.5060 - val_acc: 0.5000
Epoch 32/50
900/900 [==============================] - 1s 848us/step - loss: 0.0130 - kullback_leibler_divergence: 0.0130 - acc: 1.0000 - val_loss: 2.4110 - val_kullback_leibler_divergence: 2.4110 - val_acc: 0.5200
Epoch 33/50
900/900 [==============================] - 1s 909us/step - loss: 0.0115 - kullback_leibler_divergence: 0.0115 - acc: 1.0000 - val_loss: 2.5460 - val_kullback_leibler_divergence: 2.5460 - val_acc: 0.4700
Epoch 34/50
900/900 [==============================] - 1s 950us/step - loss: 0.0103 - kullback_leibler_divergence: 0.0103 - acc: 1.0000 - val_loss: 2.5445 - val_kullback_leibler_divergence: 2.5445 - val_acc: 0.4900
Epoch 35/50
900/900 [==============================] - 1s 887us/step - loss: 0.0094 - kullback_leibler_divergence: 0.0094 - acc: 1.0000 - val_loss: 2.5665 - val_kullback_leibler_divergence: 2.5665 - val_acc: 0.4900
Epoch 36/50
900/900 [==============================] - 1s 859us/step - loss: 0.0089 - kullback_leibler_divergence: 0.0089 - acc: 1.0000 - val_loss: 2.5844 - val_kullback_leibler_divergence: 2.5844 - val_acc: 0.4700
Epoch 37/50
900/900 [==============================] - 1s 886us/step - loss: 0.0082 - kullback_leibler_divergence: 0.0082 - acc: 1.0000 - val_loss: 2.6733 - val_kullback_leibler_divergence: 2.6733 - val_acc: 0.4800
Epoch 38/50
900/900 [==============================] - 1s 892us/step - loss: 0.0076 - kullback_leibler_divergence: 0.0076 - acc: 1.0000 - val_loss: 2.5939 - val_kullback_leibler_divergence: 2.5939 - val_acc: 0.5100
Epoch 39/50
900/900 [==============================] - 1s 895us/step - loss: 0.0070 - kullback_leibler_divergence: 0.0070 - acc: 1.0000 - val_loss: 2.6716 - val_kullback_leibler_divergence: 2.6716 - val_acc: 0.4700
Epoch 40/50
900/900 [==============================] - 1s 834us/step - loss: 0.0065 - kullback_leibler_divergence: 0.0065 - acc: 1.0000 - val_loss: 2.6808 - val_kullback_leibler_divergence: 2.6808 - val_acc: 0.5000
Epoch 41/50
900/900 [==============================] - 1s 862us/step - loss: 0.0060 - kullback_leibler_divergence: 0.0060 - acc: 1.0000 - val_loss: 2.6986 - val_kullback_leibler_divergence: 2.6986 - val_acc: 0.4700
Epoch 42/50
900/900 [==============================] - 1s 849us/step - loss: 0.0055 - kullback_leibler_divergence: 0.0055 - acc: 1.0000 - val_loss: 2.7342 - val_kullback_leibler_divergence: 2.7342 - val_acc: 0.4700
Epoch 43/50
900/900 [==============================] - 1s 870us/step - loss: 0.0054 - kullback_leibler_divergence: 0.0054 - acc: 1.0000 - val_loss: 2.7331 - val_kullback_leibler_divergence: 2.7331 - val_acc: 0.5100
Epoch 44/50
900/900 [==============================] - 1s 867us/step - loss: 0.0055 - kullback_leibler_divergence: 0.0055 - acc: 1.0000 - val_loss: 2.7994 - val_kullback_leibler_divergence: 2.7994 - val_acc: 0.4900
Epoch 45/50
900/900 [==============================] - 1s 867us/step - loss: 0.0048 - kullback_leibler_divergence: 0.0048 - acc: 1.0000 - val_loss: 2.7433 - val_kullback_leibler_divergence: 2.7433 - val_acc: 0.5100
Epoch 46/50
900/900 [==============================] - 1s 894us/step - loss: 0.0045 - kullback_leibler_divergence: 0.0045 - acc: 1.0000 - val_loss: 2.7818 - val_kullback_leibler_divergence: 2.7818 - val_acc: 0.5000
Epoch 47/50
900/900 [==============================] - 1s 862us/step - loss: 0.0042 - kullback_leibler_divergence: 0.0042 - acc: 1.0000 - val_loss: 2.8569 - val_kullback_leibler_divergence: 2.8569 - val_acc: 0.4700
Epoch 48/50
900/900 [==============================] - 1s 876us/step - loss: 0.0040 - kullback_leibler_divergence: 0.0040 - acc: 1.0000 - val_loss: 2.7850 - val_kullback_leibler_divergence: 2.7850 - val_acc: 0.4900
Epoch 49/50
900/900 [==============================] - 1s 894us/step - loss: 0.0037 - kullback_leibler_divergence: 0.0037 - acc: 1.0000 - val_loss: 2.8891 - val_kullback_leibler_divergence: 2.8891 - val_acc: 0.4700
Epoch 50/50
900/900 [==============================] - 1s 895us/step - loss: 0.0036 - kullback_leibler_divergence: 0.0036 - acc: 1.0000 - val_loss: 2.8526 - val_kullback_leibler_divergence: 2.8526 - val_acc: 0.4700
train data:
1000/1000 [==============================] - 0s 244us/step
kullback_leibler_divergence :  0.28830035134404897

acc :  0.947

test data:
10000/10000 [==============================] - 2s 236us/step
kullback_leibler_divergence :  4.13260492553711
acc :  0.3685
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 19:53:26.817054 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 19:53:26.959749 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 19:53:27.027813 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 19:53:27.105368 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 19:53:27.162394 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 19:53:27.167781 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 19:53:27.327733 4412749248 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 19:53:27.359322 4412749248 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 19:53:27.533752: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 2ms/step - loss: 2.1210 - kullback_leibler_divergence: 2.1210 - acc: 0.2522 - val_loss: 2.1019 - val_kullback_leibler_divergence: 2.1019 - val_acc: 0.1500
Epoch 2/50
900/900 [==============================] - 1s 840us/step - loss: 1.8719 - kullback_leibler_divergence: 1.8719 - acc: 0.3622 - val_loss: 1.9108 - val_kullback_leibler_divergence: 1.9108 - val_acc: 0.2400
Epoch 3/50
900/900 [==============================] - 1s 845us/step - loss: 1.6637 - kullback_leibler_divergence: 1.6637 - acc: 0.4378 - val_loss: 1.6535 - val_kullback_leibler_divergence: 1.6535 - val_acc: 0.4100
Epoch 4/50
900/900 [==============================] - 1s 866us/step - loss: 1.5267 - kullback_leibler_divergence: 1.5267 - acc: 0.4644 - val_loss: 1.6779 - val_kullback_leibler_divergence: 1.6779 - val_acc: 0.3400
Epoch 5/50
900/900 [==============================] - 1s 964us/step - loss: 1.4252 - kullback_leibler_divergence: 1.4252 - acc: 0.5156 - val_loss: 1.7745 - val_kullback_leibler_divergence: 1.7745 - val_acc: 0.3600
Epoch 6/50
900/900 [==============================] - 1s 1ms/step - loss: 1.2713 - kullback_leibler_divergence: 1.2713 - acc: 0.5744 - val_loss: 1.7296 - val_kullback_leibler_divergence: 1.7296 - val_acc: 0.4700
Epoch 7/50
900/900 [==============================] - 1s 855us/step - loss: 1.1278 - kullback_leibler_divergence: 1.1278 - acc: 0.6344 - val_loss: 1.4202 - val_kullback_leibler_divergence: 1.4202 - val_acc: 0.5000
Epoch 8/50
900/900 [==============================] - 1s 871us/step - loss: 1.0166 - kullback_leibler_divergence: 1.0166 - acc: 0.6756 - val_loss: 1.5205 - val_kullback_leibler_divergence: 1.5205 - val_acc: 0.4200
Epoch 9/50
900/900 [==============================] - 1s 870us/step - loss: 0.8890 - kullback_leibler_divergence: 0.8890 - acc: 0.7189 - val_loss: 1.4406 - val_kullback_leibler_divergence: 1.4406 - val_acc: 0.4800
Epoch 10/50
900/900 [==============================] - 1s 860us/step - loss: 0.7377 - kullback_leibler_divergence: 0.7377 - acc: 0.7911 - val_loss: 1.5435 - val_kullback_leibler_divergence: 1.5435 - val_acc: 0.4500
Epoch 11/50
900/900 [==============================] - 1s 856us/step - loss: 0.6361 - kullback_leibler_divergence: 0.6361 - acc: 0.8189 - val_loss: 1.6108 - val_kullback_leibler_divergence: 1.6108 - val_acc: 0.4200
Epoch 12/50
900/900 [==============================] - 1s 893us/step - loss: 0.5677 - kullback_leibler_divergence: 0.5677 - acc: 0.8478 - val_loss: 1.5201 - val_kullback_leibler_divergence: 1.5201 - val_acc: 0.4800
Epoch 13/50
900/900 [==============================] - 1s 887us/step - loss: 0.4897 - kullback_leibler_divergence: 0.4897 - acc: 0.8689 - val_loss: 1.8690 - val_kullback_leibler_divergence: 1.8690 - val_acc: 0.4700
Epoch 14/50
900/900 [==============================] - 1s 848us/step - loss: 0.4141 - kullback_leibler_divergence: 0.4141 - acc: 0.8956 - val_loss: 1.6706 - val_kullback_leibler_divergence: 1.6706 - val_acc: 0.4900
Epoch 15/50
900/900 [==============================] - 1s 830us/step - loss: 0.3662 - kullback_leibler_divergence: 0.3662 - acc: 0.9111 - val_loss: 1.6437 - val_kullback_leibler_divergence: 1.6437 - val_acc: 0.4500
Epoch 16/50
900/900 [==============================] - 1s 838us/step - loss: 0.3252 - kullback_leibler_divergence: 0.3252 - acc: 0.9178 - val_loss: 1.7042 - val_kullback_leibler_divergence: 1.7042 - val_acc: 0.4800
Epoch 17/50
900/900 [==============================] - 1s 900us/step - loss: 0.2595 - kullback_leibler_divergence: 0.2595 - acc: 0.9433 - val_loss: 1.8823 - val_kullback_leibler_divergence: 1.8823 - val_acc: 0.4600
Epoch 18/50
900/900 [==============================] - 1s 868us/step - loss: 0.1967 - kullback_leibler_divergence: 0.1967 - acc: 0.9656 - val_loss: 1.7992 - val_kullback_leibler_divergence: 1.7992 - val_acc: 0.4800
Epoch 19/50
900/900 [==============================] - 1s 852us/step - loss: 0.1711 - kullback_leibler_divergence: 0.1711 - acc: 0.9678 - val_loss: 2.0477 - val_kullback_leibler_divergence: 2.0477 - val_acc: 0.4400
Epoch 20/50
900/900 [==============================] - 1s 843us/step - loss: 0.1415 - kullback_leibler_divergence: 0.1415 - acc: 0.9722 - val_loss: 1.9321 - val_kullback_leibler_divergence: 1.9321 - val_acc: 0.4800
Epoch 21/50
900/900 [==============================] - 1s 858us/step - loss: 0.1180 - kullback_leibler_divergence: 0.1180 - acc: 0.9833 - val_loss: 2.1421 - val_kullback_leibler_divergence: 2.1421 - val_acc: 0.4500
Epoch 22/50
900/900 [==============================] - 1s 851us/step - loss: 0.0869 - kullback_leibler_divergence: 0.0869 - acc: 0.9889 - val_loss: 2.0853 - val_kullback_leibler_divergence: 2.0853 - val_acc: 0.5000
Epoch 23/50
900/900 [==============================] - 1s 862us/step - loss: 0.0720 - kullback_leibler_divergence: 0.0720 - acc: 0.9900 - val_loss: 2.1764 - val_kullback_leibler_divergence: 2.1764 - val_acc: 0.4900
Epoch 24/50
900/900 [==============================] - 1s 865us/step - loss: 0.0633 - kullback_leibler_divergence: 0.0633 - acc: 0.9933 - val_loss: 2.3463 - val_kullback_leibler_divergence: 2.3463 - val_acc: 0.5000
Epoch 25/50
900/900 [==============================] - 1s 872us/step - loss: 0.0505 - kullback_leibler_divergence: 0.0505 - acc: 0.9967 - val_loss: 2.3944 - val_kullback_leibler_divergence: 2.3944 - val_acc: 0.4800
Epoch 26/50
900/900 [==============================] - 1s 857us/step - loss: 0.0447 - kullback_leibler_divergence: 0.0447 - acc: 0.9978 - val_loss: 2.3940 - val_kullback_leibler_divergence: 2.3940 - val_acc: 0.4300
Epoch 27/50
900/900 [==============================] - 1s 881us/step - loss: 0.0421 - kullback_leibler_divergence: 0.0421 - acc: 0.9989 - val_loss: 2.4812 - val_kullback_leibler_divergence: 2.4812 - val_acc: 0.4500
Epoch 28/50
900/900 [==============================] - 1s 845us/step - loss: 0.0301 - kullback_leibler_divergence: 0.0301 - acc: 0.9978 - val_loss: 2.5447 - val_kullback_leibler_divergence: 2.5447 - val_acc: 0.4200
Epoch 29/50
900/900 [==============================] - 1s 863us/step - loss: 0.0240 - kullback_leibler_divergence: 0.0240 - acc: 0.9989 - val_loss: 2.4325 - val_kullback_leibler_divergence: 2.4325 - val_acc: 0.4900
Epoch 30/50
900/900 [==============================] - 1s 887us/step - loss: 0.0197 - kullback_leibler_divergence: 0.0197 - acc: 1.0000 - val_loss: 2.5846 - val_kullback_leibler_divergence: 2.5846 - val_acc: 0.4500
Epoch 31/50
900/900 [==============================] - 1s 896us/step - loss: 0.0167 - kullback_leibler_divergence: 0.0167 - acc: 1.0000 - val_loss: 2.6851 - val_kullback_leibler_divergence: 2.6851 - val_acc: 0.4100
Epoch 32/50
900/900 [==============================] - 1s 951us/step - loss: 0.0142 - kullback_leibler_divergence: 0.0142 - acc: 1.0000 - val_loss: 2.7076 - val_kullback_leibler_divergence: 2.7076 - val_acc: 0.4300
Epoch 33/50
900/900 [==============================] - 1s 852us/step - loss: 0.0130 - kullback_leibler_divergence: 0.0130 - acc: 1.0000 - val_loss: 2.6844 - val_kullback_leibler_divergence: 2.6844 - val_acc: 0.4400
Epoch 34/50
900/900 [==============================] - 1s 849us/step - loss: 0.0108 - kullback_leibler_divergence: 0.0108 - acc: 1.0000 - val_loss: 2.7840 - val_kullback_leibler_divergence: 2.7840 - val_acc: 0.4000
Epoch 35/50
900/900 [==============================] - 1s 837us/step - loss: 0.0095 - kullback_leibler_divergence: 0.0095 - acc: 1.0000 - val_loss: 2.7870 - val_kullback_leibler_divergence: 2.7870 - val_acc: 0.4500
Epoch 36/50
900/900 [==============================] - 1s 881us/step - loss: 0.0088 - kullback_leibler_divergence: 0.0088 - acc: 1.0000 - val_loss: 2.7884 - val_kullback_leibler_divergence: 2.7884 - val_acc: 0.4400
Epoch 37/50
900/900 [==============================] - 1s 841us/step - loss: 0.0080 - kullback_leibler_divergence: 0.0080 - acc: 1.0000 - val_loss: 2.9455 - val_kullback_leibler_divergence: 2.9455 - val_acc: 0.4000
Epoch 38/50
900/900 [==============================] - 1s 846us/step - loss: 0.0073 - kullback_leibler_divergence: 0.0073 - acc: 1.0000 - val_loss: 2.8362 - val_kullback_leibler_divergence: 2.8362 - val_acc: 0.4500
Epoch 39/50
900/900 [==============================] - 1s 820us/step - loss: 0.0066 - kullback_leibler_divergence: 0.0066 - acc: 1.0000 - val_loss: 2.8892 - val_kullback_leibler_divergence: 2.8892 - val_acc: 0.3900
Epoch 40/50
900/900 [==============================] - 1s 857us/step - loss: 0.0061 - kullback_leibler_divergence: 0.0061 - acc: 1.0000 - val_loss: 2.9316 - val_kullback_leibler_divergence: 2.9316 - val_acc: 0.4500
Epoch 41/50
900/900 [==============================] - 1s 848us/step - loss: 0.0056 - kullback_leibler_divergence: 0.0056 - acc: 1.0000 - val_loss: 2.9200 - val_kullback_leibler_divergence: 2.9200 - val_acc: 0.4400
Epoch 42/50
900/900 [==============================] - 1s 864us/step - loss: 0.0053 - kullback_leibler_divergence: 0.0053 - acc: 1.0000 - val_loss: 2.9749 - val_kullback_leibler_divergence: 2.9749 - val_acc: 0.4300
Epoch 43/50
900/900 [==============================] - 1s 869us/step - loss: 0.0050 - kullback_leibler_divergence: 0.0050 - acc: 1.0000 - val_loss: 3.0464 - val_kullback_leibler_divergence: 3.0464 - val_acc: 0.4200
Epoch 44/50
900/900 [==============================] - 1s 897us/step - loss: 0.0048 - kullback_leibler_divergence: 0.0048 - acc: 1.0000 - val_loss: 2.9721 - val_kullback_leibler_divergence: 2.9721 - val_acc: 0.4400
Epoch 45/50
900/900 [==============================] - 1s 893us/step - loss: 0.0046 - kullback_leibler_divergence: 0.0046 - acc: 1.0000 - val_loss: 3.0186 - val_kullback_leibler_divergence: 3.0186 - val_acc: 0.4100
Epoch 46/50
900/900 [==============================] - 1s 882us/step - loss: 0.0043 - kullback_leibler_divergence: 0.0043 - acc: 1.0000 - val_loss: 3.0650 - val_kullback_leibler_divergence: 3.0650 - val_acc: 0.4500
Epoch 47/50
900/900 [==============================] - 1s 886us/step - loss: 0.0041 - kullback_leibler_divergence: 0.0041 - acc: 1.0000 - val_loss: 3.0888 - val_kullback_leibler_divergence: 3.0888 - val_acc: 0.4000
Epoch 48/50
900/900 [==============================] - 1s 879us/step - loss: 0.0041 - kullback_leibler_divergence: 0.0041 - acc: 1.0000 - val_loss: 3.0147 - val_kullback_leibler_divergence: 3.0147 - val_acc: 0.4600
Epoch 49/50
900/900 [==============================] - 1s 849us/step - loss: 0.0038 - kullback_leibler_divergence: 0.0038 - acc: 1.0000 - val_loss: 3.1973 - val_kullback_leibler_divergence: 3.1973 - val_acc: 0.4000
Epoch 50/50
900/900 [==============================] - 1s 837us/step - loss: 0.0035 - kullback_leibler_divergence: 0.0035 - acc: 1.0000 - val_loss: 3.0682 - val_kullback_leibler_divergence: 3.0682 - val_acc: 0.4500
train data:
1000/1000 [==============================] - 0s 401us/step
kullback_leibler_divergence :  0.30974187345057724

acc :  0.945

test data:
10000/10000 [==============================] - 3s 305us/step
kullback_leibler_divergence :  4.257647859954834
acc :  0.3579
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 44
    label = np.argmax(Y_train,axis=1)
                                    ^
IndentationError: unindent does not match any outer indentation level
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
  File "imageBC.py", line 44
    for i in range(X_train.shape[0] -1 ):
                                        ^
IndentationError: unindent does not match any outer indentation level
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 21:20:13.526381 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 21:20:13.587566 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 21:20:13.604261 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 21:20:13.634708 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 21:20:13.694544 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 21:20:13.699854 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 21:20:13.812901 4598269376 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
W0626 21:20:13.844588 4598269376 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:986: The name tf.assign_add is deprecated. Please use tf.compat.v1.assign_add instead.

Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 21:20:14.018880: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 2ms/step - loss: 2.1828 - kullback_leibler_divergence: 2.1828 - acc: 0.1678 - val_loss: 2.2101 - val_kullback_leibler_divergence: 2.2101 - val_acc: 0.0200
Epoch 2/50
900/900 [==============================] - 1s 839us/step - loss: 2.0255 - kullback_leibler_divergence: 2.0255 - acc: 0.2644 - val_loss: 2.0207 - val_kullback_leibler_divergence: 2.0207 - val_acc: 0.1500
Epoch 3/50
900/900 [==============================] - 1s 825us/step - loss: 1.8354 - kullback_leibler_divergence: 1.8354 - acc: 0.3844 - val_loss: 1.7829 - val_kullback_leibler_divergence: 1.7829 - val_acc: 0.4200
Epoch 4/50
900/900 [==============================] - 1s 840us/step - loss: 1.6270 - kullback_leibler_divergence: 1.6270 - acc: 0.4567 - val_loss: 1.7250 - val_kullback_leibler_divergence: 1.7250 - val_acc: 0.3700
Epoch 5/50
900/900 [==============================] - 1s 886us/step - loss: 1.4458 - kullback_leibler_divergence: 1.4458 - acc: 0.5122 - val_loss: 1.6381 - val_kullback_leibler_divergence: 1.6381 - val_acc: 0.4400
Epoch 6/50
900/900 [==============================] - 1s 879us/step - loss: 1.3316 - kullback_leibler_divergence: 1.3316 - acc: 0.5656 - val_loss: 1.5077 - val_kullback_leibler_divergence: 1.5077 - val_acc: 0.5200
Epoch 7/50
900/900 [==============================] - 1s 839us/step - loss: 1.2277 - kullback_leibler_divergence: 1.2277 - acc: 0.5911 - val_loss: 1.5683 - val_kullback_leibler_divergence: 1.5683 - val_acc: 0.4800
Epoch 8/50
900/900 [==============================] - 1s 868us/step - loss: 1.0780 - kullback_leibler_divergence: 1.0780 - acc: 0.6667 - val_loss: 1.7499 - val_kullback_leibler_divergence: 1.7499 - val_acc: 0.4100
Epoch 9/50
900/900 [==============================] - 1s 841us/step - loss: 0.9548 - kullback_leibler_divergence: 0.9548 - acc: 0.7111 - val_loss: 1.5481 - val_kullback_leibler_divergence: 1.5481 - val_acc: 0.4600
Epoch 10/50
900/900 [==============================] - 1s 869us/step - loss: 0.8323 - kullback_leibler_divergence: 0.8323 - acc: 0.7456 - val_loss: 1.4280 - val_kullback_leibler_divergence: 1.4280 - val_acc: 0.5000
Epoch 11/50
900/900 [==============================] - 1s 857us/step - loss: 0.7245 - kullback_leibler_divergence: 0.7245 - acc: 0.7756 - val_loss: 1.4541 - val_kullback_leibler_divergence: 1.4541 - val_acc: 0.5400
Epoch 12/50
900/900 [==============================] - 1s 866us/step - loss: 0.6159 - kullback_leibler_divergence: 0.6159 - acc: 0.8322 - val_loss: 1.4328 - val_kullback_leibler_divergence: 1.4328 - val_acc: 0.5100
Epoch 13/50
900/900 [==============================] - 1s 865us/step - loss: 0.5583 - kullback_leibler_divergence: 0.5583 - acc: 0.8422 - val_loss: 1.6027 - val_kullback_leibler_divergence: 1.6027 - val_acc: 0.4700
Epoch 14/50
900/900 [==============================] - 1s 868us/step - loss: 0.4720 - kullback_leibler_divergence: 0.4720 - acc: 0.8644 - val_loss: 1.6326 - val_kullback_leibler_divergence: 1.6326 - val_acc: 0.4600
Epoch 15/50
900/900 [==============================] - 1s 860us/step - loss: 0.4125 - kullback_leibler_divergence: 0.4125 - acc: 0.8856 - val_loss: 1.8615 - val_kullback_leibler_divergence: 1.8615 - val_acc: 0.4600
Epoch 16/50
900/900 [==============================] - 1s 867us/step - loss: 0.3732 - kullback_leibler_divergence: 0.3732 - acc: 0.8944 - val_loss: 1.6320 - val_kullback_leibler_divergence: 1.6320 - val_acc: 0.4900
Epoch 17/50
900/900 [==============================] - 1s 856us/step - loss: 0.2980 - kullback_leibler_divergence: 0.2980 - acc: 0.9278 - val_loss: 1.6479 - val_kullback_leibler_divergence: 1.6479 - val_acc: 0.5000
Epoch 18/50
900/900 [==============================] - 1s 843us/step - loss: 0.2180 - kullback_leibler_divergence: 0.2180 - acc: 0.9600 - val_loss: 1.6181 - val_kullback_leibler_divergence: 1.6181 - val_acc: 0.5300
Epoch 19/50
900/900 [==============================] - 1s 844us/step - loss: 0.1855 - kullback_leibler_divergence: 0.1855 - acc: 0.9633 - val_loss: 1.6222 - val_kullback_leibler_divergence: 1.6222 - val_acc: 0.5200
Epoch 20/50
900/900 [==============================] - 1s 853us/step - loss: 0.1505 - kullback_leibler_divergence: 0.1505 - acc: 0.9811 - val_loss: 1.8367 - val_kullback_leibler_divergence: 1.8367 - val_acc: 0.4600
Epoch 21/50
900/900 [==============================] - 1s 881us/step - loss: 0.1235 - kullback_leibler_divergence: 0.1235 - acc: 0.9867 - val_loss: 1.9553 - val_kullback_leibler_divergence: 1.9553 - val_acc: 0.4900
Epoch 22/50
900/900 [==============================] - 1s 865us/step - loss: 0.1069 - kullback_leibler_divergence: 0.1069 - acc: 0.9856 - val_loss: 2.0773 - val_kullback_leibler_divergence: 2.0773 - val_acc: 0.4600
Epoch 23/50
900/900 [==============================] - 1s 877us/step - loss: 0.0901 - kullback_leibler_divergence: 0.0901 - acc: 0.9867 - val_loss: 1.8903 - val_kullback_leibler_divergence: 1.8903 - val_acc: 0.5500
Epoch 24/50
900/900 [==============================] - 1s 851us/step - loss: 0.0740 - kullback_leibler_divergence: 0.0740 - acc: 0.9956 - val_loss: 1.9658 - val_kullback_leibler_divergence: 1.9658 - val_acc: 0.4900
Epoch 25/50
900/900 [==============================] - 1s 876us/step - loss: 0.0558 - kullback_leibler_divergence: 0.0558 - acc: 0.9989 - val_loss: 2.2710 - val_kullback_leibler_divergence: 2.2710 - val_acc: 0.4700
Epoch 26/50
900/900 [==============================] - 1s 873us/step - loss: 0.0481 - kullback_leibler_divergence: 0.0481 - acc: 0.9978 - val_loss: 2.2373 - val_kullback_leibler_divergence: 2.2373 - val_acc: 0.4600
Epoch 27/50
900/900 [==============================] - 1s 877us/step - loss: 0.0378 - kullback_leibler_divergence: 0.0378 - acc: 1.0000 - val_loss: 2.0556 - val_kullback_leibler_divergence: 2.0556 - val_acc: 0.4900
Epoch 28/50
900/900 [==============================] - 1s 884us/step - loss: 0.0327 - kullback_leibler_divergence: 0.0327 - acc: 1.0000 - val_loss: 2.2284 - val_kullback_leibler_divergence: 2.2284 - val_acc: 0.4700
Epoch 29/50
900/900 [==============================] - 1s 866us/step - loss: 0.0254 - kullback_leibler_divergence: 0.0254 - acc: 1.0000 - val_loss: 2.3242 - val_kullback_leibler_divergence: 2.3242 - val_acc: 0.4600
Epoch 30/50
900/900 [==============================] - 1s 866us/step - loss: 0.0230 - kullback_leibler_divergence: 0.0230 - acc: 1.0000 - val_loss: 2.4278 - val_kullback_leibler_divergence: 2.4278 - val_acc: 0.4600
Epoch 31/50
900/900 [==============================] - 1s 863us/step - loss: 0.0207 - kullback_leibler_divergence: 0.0207 - acc: 1.0000 - val_loss: 2.3746 - val_kullback_leibler_divergence: 2.3746 - val_acc: 0.4500
Epoch 32/50
900/900 [==============================] - 1s 847us/step - loss: 0.0177 - kullback_leibler_divergence: 0.0177 - acc: 1.0000 - val_loss: 2.3033 - val_kullback_leibler_divergence: 2.3033 - val_acc: 0.4700
Epoch 33/50
900/900 [==============================] - 1s 838us/step - loss: 0.0154 - kullback_leibler_divergence: 0.0154 - acc: 1.0000 - val_loss: 2.3761 - val_kullback_leibler_divergence: 2.3761 - val_acc: 0.4700
Epoch 34/50
900/900 [==============================] - 1s 851us/step - loss: 0.0141 - kullback_leibler_divergence: 0.0141 - acc: 1.0000 - val_loss: 2.5601 - val_kullback_leibler_divergence: 2.5601 - val_acc: 0.4800
Epoch 35/50
900/900 [==============================] - 1s 882us/step - loss: 0.0127 - kullback_leibler_divergence: 0.0127 - acc: 1.0000 - val_loss: 2.5477 - val_kullback_leibler_divergence: 2.5477 - val_acc: 0.4800
Epoch 36/50
900/900 [==============================] - 1s 879us/step - loss: 0.0116 - kullback_leibler_divergence: 0.0116 - acc: 1.0000 - val_loss: 2.4450 - val_kullback_leibler_divergence: 2.4450 - val_acc: 0.4700
Epoch 37/50
900/900 [==============================] - 1s 891us/step - loss: 0.0101 - kullback_leibler_divergence: 0.0101 - acc: 1.0000 - val_loss: 2.5910 - val_kullback_leibler_divergence: 2.5910 - val_acc: 0.4500
Epoch 38/50
900/900 [==============================] - 1s 842us/step - loss: 0.0093 - kullback_leibler_divergence: 0.0093 - acc: 1.0000 - val_loss: 2.5661 - val_kullback_leibler_divergence: 2.5661 - val_acc: 0.4500
Epoch 39/50
900/900 [==============================] - 1s 882us/step - loss: 0.0084 - kullback_leibler_divergence: 0.0084 - acc: 1.0000 - val_loss: 2.5803 - val_kullback_leibler_divergence: 2.5803 - val_acc: 0.4600
Epoch 40/50
900/900 [==============================] - 1s 853us/step - loss: 0.0081 - kullback_leibler_divergence: 0.0081 - acc: 1.0000 - val_loss: 2.5684 - val_kullback_leibler_divergence: 2.5684 - val_acc: 0.4800
Epoch 41/50
900/900 [==============================] - 1s 880us/step - loss: 0.0073 - kullback_leibler_divergence: 0.0073 - acc: 1.0000 - val_loss: 2.5989 - val_kullback_leibler_divergence: 2.5989 - val_acc: 0.4700
Epoch 42/50
900/900 [==============================] - 1s 866us/step - loss: 0.0069 - kullback_leibler_divergence: 0.0069 - acc: 1.0000 - val_loss: 2.7112 - val_kullback_leibler_divergence: 2.7112 - val_acc: 0.4600
Epoch 43/50
900/900 [==============================] - 1s 884us/step - loss: 0.0064 - kullback_leibler_divergence: 0.0064 - acc: 1.0000 - val_loss: 2.6683 - val_kullback_leibler_divergence: 2.6683 - val_acc: 0.4800
Epoch 44/50
900/900 [==============================] - 1s 928us/step - loss: 0.0059 - kullback_leibler_divergence: 0.0059 - acc: 1.0000 - val_loss: 2.6586 - val_kullback_leibler_divergence: 2.6586 - val_acc: 0.4600
Epoch 45/50
900/900 [==============================] - 1s 849us/step - loss: 0.0056 - kullback_leibler_divergence: 0.0056 - acc: 1.0000 - val_loss: 2.7202 - val_kullback_leibler_divergence: 2.7202 - val_acc: 0.4500
Epoch 46/50
900/900 [==============================] - 1s 863us/step - loss: 0.0054 - kullback_leibler_divergence: 0.0054 - acc: 1.0000 - val_loss: 2.6742 - val_kullback_leibler_divergence: 2.6742 - val_acc: 0.4700
Epoch 47/50
900/900 [==============================] - 1s 851us/step - loss: 0.0051 - kullback_leibler_divergence: 0.0051 - acc: 1.0000 - val_loss: 2.8070 - val_kullback_leibler_divergence: 2.8070 - val_acc: 0.4700
Epoch 48/50
900/900 [==============================] - 1s 867us/step - loss: 0.0047 - kullback_leibler_divergence: 0.0047 - acc: 1.0000 - val_loss: 2.6977 - val_kullback_leibler_divergence: 2.6977 - val_acc: 0.4900
Epoch 49/50
900/900 [==============================] - 1s 875us/step - loss: 0.0045 - kullback_leibler_divergence: 0.0045 - acc: 1.0000 - val_loss: 2.8167 - val_kullback_leibler_divergence: 2.8167 - val_acc: 0.4700
Epoch 50/50
900/900 [==============================] - 1s 833us/step - loss: 0.0044 - kullback_leibler_divergence: 0.0044 - acc: 1.0000 - val_loss: 2.7796 - val_kullback_leibler_divergence: 2.7796 - val_acc: 0.4700
train data:
1000/1000 [==============================] - 0s 243us/step
kullback_leibler_divergence :  0.2814900751337409

acc :  0.947

test data:
10000/10000 [==============================] - 2s 234us/step
kullback_leibler_divergence :  4.0110004585266115
acc :  0.3668
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 21:23:08.956323 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 21:23:08.977045 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 21:23:08.982014 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 21:23:09.010169 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 21:23:09.069173 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 21:23:09.076498 4542338496 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 21:23:09.120328 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 21:23:09.127813 4542338496 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 30, 30, 32)        9248      
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 15, 15, 32)        0         
_________________________________________________________________
conv2d_3 (Conv2D)            (None, 15, 15, 64)        18496     
_________________________________________________________________
conv2d_4 (Conv2D)            (None, 15, 15, 64)        36928     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 7, 7, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 3136)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               1606144   
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 1,676,842
Trainable params: 1,676,842
Non-trainable params: 0
_________________________________________________________________
W0626 21:23:09.238692 4542338496 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 21:23:09.546986: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 2s 2ms/step - loss: 2.1516 - kullback_leibler_divergence: 2.1516 - acc: 0.2067 - val_loss: 2.1736 - val_kullback_leibler_divergence: 2.1736 - val_acc: 0.1400
Epoch 2/50
900/900 [==============================] - 2s 2ms/step - loss: 1.9993 - kullback_leibler_divergence: 1.9993 - acc: 0.2933 - val_loss: 2.0284 - val_kullback_leibler_divergence: 2.0284 - val_acc: 0.2300
Epoch 3/50
900/900 [==============================] - 2s 2ms/step - loss: 1.8721 - kullback_leibler_divergence: 1.8721 - acc: 0.3544 - val_loss: 2.0476 - val_kullback_leibler_divergence: 2.0476 - val_acc: 0.2200
Epoch 4/50
900/900 [==============================] - 2s 2ms/step - loss: 1.7419 - kullback_leibler_divergence: 1.7419 - acc: 0.3978 - val_loss: 1.9379 - val_kullback_leibler_divergence: 1.9379 - val_acc: 0.2900
Epoch 5/50
900/900 [==============================] - 2s 2ms/step - loss: 1.6113 - kullback_leibler_divergence: 1.6113 - acc: 0.4456 - val_loss: 1.6824 - val_kullback_leibler_divergence: 1.6824 - val_acc: 0.4400
Epoch 6/50
900/900 [==============================] - 2s 2ms/step - loss: 1.4664 - kullback_leibler_divergence: 1.4664 - acc: 0.4933 - val_loss: 1.6350 - val_kullback_leibler_divergence: 1.6350 - val_acc: 0.3600
Epoch 7/50
900/900 [==============================] - 2s 2ms/step - loss: 1.3562 - kullback_leibler_divergence: 1.3562 - acc: 0.5389 - val_loss: 1.5192 - val_kullback_leibler_divergence: 1.5192 - val_acc: 0.4300
Epoch 8/50
900/900 [==============================] - 2s 2ms/step - loss: 1.2540 - kullback_leibler_divergence: 1.2540 - acc: 0.5633 - val_loss: 1.6166 - val_kullback_leibler_divergence: 1.6166 - val_acc: 0.3700
Epoch 9/50
900/900 [==============================] - 2s 2ms/step - loss: 1.1273 - kullback_leibler_divergence: 1.1273 - acc: 0.6022 - val_loss: 1.8790 - val_kullback_leibler_divergence: 1.8790 - val_acc: 0.3800
Epoch 10/50
900/900 [==============================] - 2s 2ms/step - loss: 1.0358 - kullback_leibler_divergence: 1.0358 - acc: 0.6322 - val_loss: 1.5488 - val_kullback_leibler_divergence: 1.5488 - val_acc: 0.4600
Epoch 11/50
900/900 [==============================] - 2s 2ms/step - loss: 0.9470 - kullback_leibler_divergence: 0.9470 - acc: 0.6844 - val_loss: 1.6317 - val_kullback_leibler_divergence: 1.6317 - val_acc: 0.4300
Epoch 12/50
900/900 [==============================] - 2s 2ms/step - loss: 0.8258 - kullback_leibler_divergence: 0.8258 - acc: 0.7233 - val_loss: 1.6676 - val_kullback_leibler_divergence: 1.6676 - val_acc: 0.4000
Epoch 13/50
900/900 [==============================] - 2s 2ms/step - loss: 0.7130 - kullback_leibler_divergence: 0.7130 - acc: 0.7644 - val_loss: 1.8556 - val_kullback_leibler_divergence: 1.8556 - val_acc: 0.4000
Epoch 14/50
900/900 [==============================] - 2s 2ms/step - loss: 0.5946 - kullback_leibler_divergence: 0.5946 - acc: 0.8089 - val_loss: 2.0531 - val_kullback_leibler_divergence: 2.0531 - val_acc: 0.3700
Epoch 15/50
900/900 [==============================] - 2s 2ms/step - loss: 0.4814 - kullback_leibler_divergence: 0.4814 - acc: 0.8333 - val_loss: 1.7823 - val_kullback_leibler_divergence: 1.7823 - val_acc: 0.4100
Epoch 16/50
900/900 [==============================] - 2s 2ms/step - loss: 0.4117 - kullback_leibler_divergence: 0.4117 - acc: 0.8578 - val_loss: 1.9026 - val_kullback_leibler_divergence: 1.9026 - val_acc: 0.4600
Epoch 17/50
900/900 [==============================] - 2s 2ms/step - loss: 0.2895 - kullback_leibler_divergence: 0.2895 - acc: 0.9167 - val_loss: 2.0757 - val_kullback_leibler_divergence: 2.0757 - val_acc: 0.4000
Epoch 18/50
900/900 [==============================] - 2s 2ms/step - loss: 0.2542 - kullback_leibler_divergence: 0.2542 - acc: 0.9167 - val_loss: 2.2795 - val_kullback_leibler_divergence: 2.2795 - val_acc: 0.4600
Epoch 19/50
900/900 [==============================] - 2s 2ms/step - loss: 0.2335 - kullback_leibler_divergence: 0.2335 - acc: 0.9233 - val_loss: 2.1560 - val_kullback_leibler_divergence: 2.1560 - val_acc: 0.4800
Epoch 20/50
900/900 [==============================] - 2s 2ms/step - loss: 0.1966 - kullback_leibler_divergence: 0.1966 - acc: 0.9411 - val_loss: 2.5309 - val_kullback_leibler_divergence: 2.5309 - val_acc: 0.4100
Epoch 21/50
900/900 [==============================] - 2s 2ms/step - loss: 0.1706 - kullback_leibler_divergence: 0.1706 - acc: 0.9522 - val_loss: 2.3401 - val_kullback_leibler_divergence: 2.3401 - val_acc: 0.4400
Epoch 22/50
900/900 [==============================] - 2s 2ms/step - loss: 0.1636 - kullback_leibler_divergence: 0.1636 - acc: 0.9589 - val_loss: 2.5021 - val_kullback_leibler_divergence: 2.5021 - val_acc: 0.4000
Epoch 23/50
900/900 [==============================] - 2s 2ms/step - loss: 0.1373 - kullback_leibler_divergence: 0.1373 - acc: 0.9644 - val_loss: 2.6437 - val_kullback_leibler_divergence: 2.6437 - val_acc: 0.4300
Epoch 24/50
900/900 [==============================] - 2s 2ms/step - loss: 0.1059 - kullback_leibler_divergence: 0.1059 - acc: 0.9622 - val_loss: 2.9432 - val_kullback_leibler_divergence: 2.9432 - val_acc: 0.3700
Epoch 25/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0757 - kullback_leibler_divergence: 0.0757 - acc: 0.9800 - val_loss: 2.8403 - val_kullback_leibler_divergence: 2.8403 - val_acc: 0.3900
Epoch 26/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0667 - kullback_leibler_divergence: 0.0667 - acc: 0.9833 - val_loss: 2.9130 - val_kullback_leibler_divergence: 2.9130 - val_acc: 0.3700
Epoch 27/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0443 - kullback_leibler_divergence: 0.0443 - acc: 0.9889 - val_loss: 3.3011 - val_kullback_leibler_divergence: 3.3011 - val_acc: 0.3900
Epoch 28/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0503 - kullback_leibler_divergence: 0.0503 - acc: 0.9889 - val_loss: 3.3935 - val_kullback_leibler_divergence: 3.3935 - val_acc: 0.3900
Epoch 29/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0477 - kullback_leibler_divergence: 0.0477 - acc: 0.9878 - val_loss: 3.0269 - val_kullback_leibler_divergence: 3.0269 - val_acc: 0.4300
Epoch 30/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0397 - kullback_leibler_divergence: 0.0397 - acc: 0.9889 - val_loss: 3.6823 - val_kullback_leibler_divergence: 3.6823 - val_acc: 0.3700
Epoch 31/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0437 - kullback_leibler_divergence: 0.0437 - acc: 0.9889 - val_loss: 3.1092 - val_kullback_leibler_divergence: 3.1092 - val_acc: 0.4000
Epoch 32/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0243 - kullback_leibler_divergence: 0.0243 - acc: 0.9956 - val_loss: 3.3647 - val_kullback_leibler_divergence: 3.3647 - val_acc: 0.4000
Epoch 33/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0435 - kullback_leibler_divergence: 0.0435 - acc: 0.9844 - val_loss: 3.9326 - val_kullback_leibler_divergence: 3.9326 - val_acc: 0.3700
Epoch 34/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0423 - kullback_leibler_divergence: 0.0423 - acc: 0.9878 - val_loss: 3.1611 - val_kullback_leibler_divergence: 3.1611 - val_acc: 0.4100
Epoch 35/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0307 - kullback_leibler_divergence: 0.0307 - acc: 0.9922 - val_loss: 3.4396 - val_kullback_leibler_divergence: 3.4396 - val_acc: 0.3900
Epoch 36/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0278 - kullback_leibler_divergence: 0.0278 - acc: 0.9933 - val_loss: 3.2765 - val_kullback_leibler_divergence: 3.2765 - val_acc: 0.4200
Epoch 37/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0359 - kullback_leibler_divergence: 0.0359 - acc: 0.9911 - val_loss: 3.9067 - val_kullback_leibler_divergence: 3.9067 - val_acc: 0.3800
Epoch 38/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0372 - kullback_leibler_divergence: 0.0372 - acc: 0.9900 - val_loss: 3.5193 - val_kullback_leibler_divergence: 3.5193 - val_acc: 0.4200
Epoch 39/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0331 - kullback_leibler_divergence: 0.0331 - acc: 0.9889 - val_loss: 3.4330 - val_kullback_leibler_divergence: 3.4330 - val_acc: 0.4400
Epoch 40/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0334 - kullback_leibler_divergence: 0.0334 - acc: 0.9922 - val_loss: 3.7095 - val_kullback_leibler_divergence: 3.7095 - val_acc: 0.3600
Epoch 41/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0220 - kullback_leibler_divergence: 0.0220 - acc: 0.9956 - val_loss: 3.6013 - val_kullback_leibler_divergence: 3.6013 - val_acc: 0.3900
Epoch 42/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0183 - kullback_leibler_divergence: 0.0183 - acc: 0.9967 - val_loss: 3.6312 - val_kullback_leibler_divergence: 3.6312 - val_acc: 0.4100
Epoch 43/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0188 - kullback_leibler_divergence: 0.0188 - acc: 0.9956 - val_loss: 3.6498 - val_kullback_leibler_divergence: 3.6498 - val_acc: 0.4200
Epoch 44/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0200 - kullback_leibler_divergence: 0.0200 - acc: 0.9922 - val_loss: 3.4917 - val_kullback_leibler_divergence: 3.4917 - val_acc: 0.4200
Epoch 45/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0333 - kullback_leibler_divergence: 0.0333 - acc: 0.9878 - val_loss: 3.8024 - val_kullback_leibler_divergence: 3.8024 - val_acc: 0.3800
Epoch 46/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0152 - kullback_leibler_divergence: 0.0152 - acc: 0.9978 - val_loss: 3.8647 - val_kullback_leibler_divergence: 3.8647 - val_acc: 0.4100
Epoch 47/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0184 - kullback_leibler_divergence: 0.0184 - acc: 0.9967 - val_loss: 3.8812 - val_kullback_leibler_divergence: 3.8812 - val_acc: 0.4500
Epoch 48/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0179 - kullback_leibler_divergence: 0.0179 - acc: 0.9922 - val_loss: 4.7407 - val_kullback_leibler_divergence: 4.7407 - val_acc: 0.3400
Epoch 49/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0253 - kullback_leibler_divergence: 0.0253 - acc: 0.9922 - val_loss: 3.2820 - val_kullback_leibler_divergence: 3.2820 - val_acc: 0.4300
Epoch 50/50
900/900 [==============================] - 2s 2ms/step - loss: 0.0212 - kullback_leibler_divergence: 0.0212 - acc: 0.9944 - val_loss: 3.8840 - val_kullback_leibler_divergence: 3.8840 - val_acc: 0.3600
train data:
1000/1000 [==============================] - 1s 515us/step
kullback_leibler_divergence :  0.38981313862651584

acc :  0.936

test data:
10000/10000 [==============================] - 5s 499us/step
kullback_leibler_divergence :  4.814072445678711
acc :  0.3455
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 21:27:22.303189 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 21:27:22.315513 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 21:27:22.317075 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 21:27:22.328092 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 21:27:22.355423 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 21:27:22.361672 4612781504 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 21:27:22.394258 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 21:27:22.399899 4612781504 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 21:27:22.494565 4612781504 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 21:27:22.716969: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.1256 - kullback_leibler_divergence: 2.1256 - acc: 0.2267 - val_loss: 2.0941 - val_kullback_leibler_divergence: 2.0941 - val_acc: 0.1800
Epoch 2/50
900/900 [==============================] - 1s 885us/step - loss: 1.9495 - kullback_leibler_divergence: 1.9495 - acc: 0.3100 - val_loss: 1.9137 - val_kullback_leibler_divergence: 1.9137 - val_acc: 0.2700
Epoch 3/50
900/900 [==============================] - 1s 893us/step - loss: 1.7800 - kullback_leibler_divergence: 1.7800 - acc: 0.4011 - val_loss: 1.8337 - val_kullback_leibler_divergence: 1.8337 - val_acc: 0.3400
Epoch 4/50
900/900 [==============================] - 1s 886us/step - loss: 1.6140 - kullback_leibler_divergence: 1.6140 - acc: 0.4533 - val_loss: 1.5903 - val_kullback_leibler_divergence: 1.5903 - val_acc: 0.4300
Epoch 5/50
900/900 [==============================] - 1s 908us/step - loss: 1.5175 - kullback_leibler_divergence: 1.5175 - acc: 0.4878 - val_loss: 1.6170 - val_kullback_leibler_divergence: 1.6170 - val_acc: 0.4200
Epoch 6/50
900/900 [==============================] - 1s 920us/step - loss: 1.3956 - kullback_leibler_divergence: 1.3956 - acc: 0.5244 - val_loss: 1.5228 - val_kullback_leibler_divergence: 1.5228 - val_acc: 0.5000
Epoch 7/50
900/900 [==============================] - 1s 925us/step - loss: 1.3032 - kullback_leibler_divergence: 1.3032 - acc: 0.5633 - val_loss: 1.5169 - val_kullback_leibler_divergence: 1.5169 - val_acc: 0.4700
Epoch 8/50
900/900 [==============================] - 1s 909us/step - loss: 1.1939 - kullback_leibler_divergence: 1.1939 - acc: 0.6078 - val_loss: 1.4174 - val_kullback_leibler_divergence: 1.4174 - val_acc: 0.4700
Epoch 9/50
900/900 [==============================] - 1s 915us/step - loss: 1.1081 - kullback_leibler_divergence: 1.1081 - acc: 0.6300 - val_loss: 1.3922 - val_kullback_leibler_divergence: 1.3922 - val_acc: 0.4700
Epoch 10/50
900/900 [==============================] - 1s 903us/step - loss: 1.0234 - kullback_leibler_divergence: 1.0234 - acc: 0.6622 - val_loss: 1.4354 - val_kullback_leibler_divergence: 1.4354 - val_acc: 0.5100
Epoch 11/50
900/900 [==============================] - 1s 918us/step - loss: 0.9389 - kullback_leibler_divergence: 0.9389 - acc: 0.6944 - val_loss: 1.4920 - val_kullback_leibler_divergence: 1.4920 - val_acc: 0.4700
Epoch 12/50
900/900 [==============================] - 1s 897us/step - loss: 0.8946 - kullback_leibler_divergence: 0.8946 - acc: 0.7178 - val_loss: 1.4800 - val_kullback_leibler_divergence: 1.4800 - val_acc: 0.4800
Epoch 13/50
900/900 [==============================] - 1s 898us/step - loss: 0.7876 - kullback_leibler_divergence: 0.7876 - acc: 0.7533 - val_loss: 1.3736 - val_kullback_leibler_divergence: 1.3736 - val_acc: 0.4700
Epoch 14/50
900/900 [==============================] - 1s 911us/step - loss: 0.7447 - kullback_leibler_divergence: 0.7447 - acc: 0.7611 - val_loss: 1.4682 - val_kullback_leibler_divergence: 1.4682 - val_acc: 0.4800
Epoch 15/50
900/900 [==============================] - 1s 907us/step - loss: 0.6671 - kullback_leibler_divergence: 0.6671 - acc: 0.7844 - val_loss: 1.6099 - val_kullback_leibler_divergence: 1.6099 - val_acc: 0.4100
Epoch 16/50
900/900 [==============================] - 1s 911us/step - loss: 0.5611 - kullback_leibler_divergence: 0.5611 - acc: 0.8356 - val_loss: 1.5085 - val_kullback_leibler_divergence: 1.5085 - val_acc: 0.5300
Epoch 17/50
900/900 [==============================] - 1s 902us/step - loss: 0.5165 - kullback_leibler_divergence: 0.5165 - acc: 0.8389 - val_loss: 1.4457 - val_kullback_leibler_divergence: 1.4457 - val_acc: 0.5100
Epoch 18/50
900/900 [==============================] - 1s 916us/step - loss: 0.4471 - kullback_leibler_divergence: 0.4471 - acc: 0.8733 - val_loss: 1.4123 - val_kullback_leibler_divergence: 1.4123 - val_acc: 0.5000
Epoch 19/50
900/900 [==============================] - 1s 904us/step - loss: 0.4034 - kullback_leibler_divergence: 0.4034 - acc: 0.8900 - val_loss: 1.5065 - val_kullback_leibler_divergence: 1.5065 - val_acc: 0.4900
Epoch 20/50
900/900 [==============================] - 1s 930us/step - loss: 0.3603 - kullback_leibler_divergence: 0.3603 - acc: 0.8989 - val_loss: 1.6578 - val_kullback_leibler_divergence: 1.6578 - val_acc: 0.4400
Epoch 21/50
900/900 [==============================] - 1s 909us/step - loss: 0.3153 - kullback_leibler_divergence: 0.3153 - acc: 0.9200 - val_loss: 1.6536 - val_kullback_leibler_divergence: 1.6536 - val_acc: 0.5200
Epoch 22/50
900/900 [==============================] - 1s 926us/step - loss: 0.2792 - kullback_leibler_divergence: 0.2792 - acc: 0.9278 - val_loss: 1.6028 - val_kullback_leibler_divergence: 1.6028 - val_acc: 0.4800
Epoch 23/50
900/900 [==============================] - 1s 905us/step - loss: 0.2637 - kullback_leibler_divergence: 0.2637 - acc: 0.9289 - val_loss: 1.5029 - val_kullback_leibler_divergence: 1.5029 - val_acc: 0.5300
Epoch 24/50
900/900 [==============================] - 1s 901us/step - loss: 0.2231 - kullback_leibler_divergence: 0.2231 - acc: 0.9422 - val_loss: 1.7136 - val_kullback_leibler_divergence: 1.7136 - val_acc: 0.4400
Epoch 25/50
900/900 [==============================] - 1s 939us/step - loss: 0.1940 - kullback_leibler_divergence: 0.1940 - acc: 0.9522 - val_loss: 1.7339 - val_kullback_leibler_divergence: 1.7339 - val_acc: 0.5300
Epoch 26/50
900/900 [==============================] - 1s 921us/step - loss: 0.1629 - kullback_leibler_divergence: 0.1629 - acc: 0.9622 - val_loss: 1.7806 - val_kullback_leibler_divergence: 1.7806 - val_acc: 0.4900
Epoch 27/50
900/900 [==============================] - 1s 913us/step - loss: 0.1618 - kullback_leibler_divergence: 0.1618 - acc: 0.9578 - val_loss: 1.7609 - val_kullback_leibler_divergence: 1.7609 - val_acc: 0.5400
Epoch 28/50
900/900 [==============================] - 1s 918us/step - loss: 0.1284 - kullback_leibler_divergence: 0.1284 - acc: 0.9744 - val_loss: 1.9724 - val_kullback_leibler_divergence: 1.9724 - val_acc: 0.4000
Epoch 29/50
900/900 [==============================] - 1s 906us/step - loss: 0.1238 - kullback_leibler_divergence: 0.1238 - acc: 0.9744 - val_loss: 1.9491 - val_kullback_leibler_divergence: 1.9491 - val_acc: 0.4700
Epoch 30/50
900/900 [==============================] - 1s 949us/step - loss: 0.0943 - kullback_leibler_divergence: 0.0943 - acc: 0.9867 - val_loss: 2.3228 - val_kullback_leibler_divergence: 2.3228 - val_acc: 0.4700
Epoch 31/50
900/900 [==============================] - 1s 899us/step - loss: 0.1080 - kullback_leibler_divergence: 0.1080 - acc: 0.9744 - val_loss: 2.0387 - val_kullback_leibler_divergence: 2.0387 - val_acc: 0.4900
Epoch 32/50
900/900 [==============================] - 1s 943us/step - loss: 0.0951 - kullback_leibler_divergence: 0.0951 - acc: 0.9833 - val_loss: 2.1178 - val_kullback_leibler_divergence: 2.1178 - val_acc: 0.4500
Epoch 33/50
900/900 [==============================] - 1s 913us/step - loss: 0.0725 - kullback_leibler_divergence: 0.0725 - acc: 0.9911 - val_loss: 2.1776 - val_kullback_leibler_divergence: 2.1776 - val_acc: 0.4600
Epoch 34/50
900/900 [==============================] - 1s 909us/step - loss: 0.0724 - kullback_leibler_divergence: 0.0724 - acc: 0.9878 - val_loss: 2.4448 - val_kullback_leibler_divergence: 2.4448 - val_acc: 0.4100
Epoch 35/50
900/900 [==============================] - 1s 930us/step - loss: 0.0779 - kullback_leibler_divergence: 0.0779 - acc: 0.9844 - val_loss: 2.3724 - val_kullback_leibler_divergence: 2.3724 - val_acc: 0.4700
Epoch 36/50
900/900 [==============================] - 1s 917us/step - loss: 0.0588 - kullback_leibler_divergence: 0.0588 - acc: 0.9911 - val_loss: 1.9221 - val_kullback_leibler_divergence: 1.9221 - val_acc: 0.5000
Epoch 37/50
900/900 [==============================] - 1s 893us/step - loss: 0.0620 - kullback_leibler_divergence: 0.0620 - acc: 0.9867 - val_loss: 2.4628 - val_kullback_leibler_divergence: 2.4628 - val_acc: 0.4400
Epoch 38/50
900/900 [==============================] - 1s 919us/step - loss: 0.0502 - kullback_leibler_divergence: 0.0502 - acc: 0.9933 - val_loss: 2.4960 - val_kullback_leibler_divergence: 2.4960 - val_acc: 0.4400
Epoch 39/50
900/900 [==============================] - 1s 915us/step - loss: 0.0453 - kullback_leibler_divergence: 0.0453 - acc: 0.9956 - val_loss: 2.2341 - val_kullback_leibler_divergence: 2.2341 - val_acc: 0.4900
Epoch 40/50
900/900 [==============================] - 1s 900us/step - loss: 0.0448 - kullback_leibler_divergence: 0.0448 - acc: 0.9922 - val_loss: 2.2341 - val_kullback_leibler_divergence: 2.2341 - val_acc: 0.5100
Epoch 41/50
900/900 [==============================] - 1s 914us/step - loss: 0.0406 - kullback_leibler_divergence: 0.0406 - acc: 0.9956 - val_loss: 2.3788 - val_kullback_leibler_divergence: 2.3788 - val_acc: 0.4800
Epoch 42/50
900/900 [==============================] - 1s 920us/step - loss: 0.0425 - kullback_leibler_divergence: 0.0425 - acc: 0.9944 - val_loss: 2.2781 - val_kullback_leibler_divergence: 2.2781 - val_acc: 0.5000
Epoch 43/50
900/900 [==============================] - 1s 917us/step - loss: 0.0326 - kullback_leibler_divergence: 0.0326 - acc: 0.9978 - val_loss: 2.4409 - val_kullback_leibler_divergence: 2.4409 - val_acc: 0.4400
Epoch 44/50
900/900 [==============================] - 1s 896us/step - loss: 0.0262 - kullback_leibler_divergence: 0.0262 - acc: 0.9989 - val_loss: 2.6284 - val_kullback_leibler_divergence: 2.6284 - val_acc: 0.4300
Epoch 45/50
900/900 [==============================] - 1s 909us/step - loss: 0.0240 - kullback_leibler_divergence: 0.0240 - acc: 0.9989 - val_loss: 2.5122 - val_kullback_leibler_divergence: 2.5122 - val_acc: 0.4900
Epoch 46/50
900/900 [==============================] - 1s 943us/step - loss: 0.0260 - kullback_leibler_divergence: 0.0260 - acc: 0.9978 - val_loss: 2.6302 - val_kullback_leibler_divergence: 2.6302 - val_acc: 0.5000
Epoch 47/50
900/900 [==============================] - 1s 912us/step - loss: 0.0279 - kullback_leibler_divergence: 0.0279 - acc: 0.9956 - val_loss: 2.6536 - val_kullback_leibler_divergence: 2.6536 - val_acc: 0.4700
Epoch 48/50
900/900 [==============================] - 1s 929us/step - loss: 0.0259 - kullback_leibler_divergence: 0.0259 - acc: 0.9989 - val_loss: 2.5083 - val_kullback_leibler_divergence: 2.5083 - val_acc: 0.4900
Epoch 49/50
900/900 [==============================] - 1s 902us/step - loss: 0.0204 - kullback_leibler_divergence: 0.0204 - acc: 0.9989 - val_loss: 2.6104 - val_kullback_leibler_divergence: 2.6104 - val_acc: 0.4800
Epoch 50/50
900/900 [==============================] - 1s 912us/step - loss: 0.0207 - kullback_leibler_divergence: 0.0207 - acc: 0.9989 - val_loss: 2.5399 - val_kullback_leibler_divergence: 2.5399 - val_acc: 0.5000
train data:
1000/1000 [==============================] - 0s 242us/step
kullback_leibler_divergence :  0.257554867643863

acc :  0.95

test data:
10000/10000 [==============================] - 2s 242us/step
kullback_leibler_divergence :  3.560052458572388
acc :  0.3739
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 21:29:45.832720 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 21:29:45.845583 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 21:29:45.847473 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 21:29:45.859535 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 21:29:45.888405 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 21:29:45.893780 4637251008 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 21:29:45.928183 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 21:29:45.933701 4637251008 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 21:29:46.029906 4637251008 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 21:29:46.254671: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.3042 - kullback_leibler_divergence: 2.3042 - acc: 0.1133 - val_loss: 2.2982 - val_kullback_leibler_divergence: 2.2982 - val_acc: 0.0800
Epoch 2/50
900/900 [==============================] - 1s 890us/step - loss: 2.1665 - kullback_leibler_divergence: 2.1665 - acc: 0.2389 - val_loss: 2.1872 - val_kullback_leibler_divergence: 2.1872 - val_acc: 0.1000
Epoch 3/50
900/900 [==============================] - 1s 897us/step - loss: 1.9856 - kullback_leibler_divergence: 1.9856 - acc: 0.2856 - val_loss: 1.9971 - val_kullback_leibler_divergence: 1.9971 - val_acc: 0.1900
Epoch 4/50
900/900 [==============================] - 1s 891us/step - loss: 1.8249 - kullback_leibler_divergence: 1.8249 - acc: 0.3333 - val_loss: 1.9039 - val_kullback_leibler_divergence: 1.9039 - val_acc: 0.1900
Epoch 5/50
900/900 [==============================] - 1s 880us/step - loss: 1.6714 - kullback_leibler_divergence: 1.6714 - acc: 0.4200 - val_loss: 1.7786 - val_kullback_leibler_divergence: 1.7786 - val_acc: 0.3400
Epoch 6/50
900/900 [==============================] - 1s 881us/step - loss: 1.5468 - kullback_leibler_divergence: 1.5468 - acc: 0.4456 - val_loss: 1.7933 - val_kullback_leibler_divergence: 1.7933 - val_acc: 0.3800
Epoch 7/50
900/900 [==============================] - 1s 926us/step - loss: 1.4548 - kullback_leibler_divergence: 1.4548 - acc: 0.4844 - val_loss: 1.7675 - val_kullback_leibler_divergence: 1.7675 - val_acc: 0.3300
Epoch 8/50
900/900 [==============================] - 1s 893us/step - loss: 1.3396 - kullback_leibler_divergence: 1.3396 - acc: 0.5411 - val_loss: 1.6826 - val_kullback_leibler_divergence: 1.6826 - val_acc: 0.4100
Epoch 9/50
900/900 [==============================] - 1s 888us/step - loss: 1.2787 - kullback_leibler_divergence: 1.2787 - acc: 0.5333 - val_loss: 1.5452 - val_kullback_leibler_divergence: 1.5452 - val_acc: 0.4800
Epoch 10/50
900/900 [==============================] - 1s 889us/step - loss: 1.2115 - kullback_leibler_divergence: 1.2115 - acc: 0.5689 - val_loss: 1.6007 - val_kullback_leibler_divergence: 1.6007 - val_acc: 0.4600
Epoch 11/50
900/900 [==============================] - 1s 896us/step - loss: 1.0940 - kullback_leibler_divergence: 1.0940 - acc: 0.6189 - val_loss: 1.7297 - val_kullback_leibler_divergence: 1.7297 - val_acc: 0.3900
Epoch 12/50
900/900 [==============================] - 1s 868us/step - loss: 1.0488 - kullback_leibler_divergence: 1.0488 - acc: 0.6400 - val_loss: 1.6446 - val_kullback_leibler_divergence: 1.6446 - val_acc: 0.4700
Epoch 13/50
900/900 [==============================] - 1s 884us/step - loss: 0.9307 - kullback_leibler_divergence: 0.9307 - acc: 0.6822 - val_loss: 1.6386 - val_kullback_leibler_divergence: 1.6386 - val_acc: 0.4500
Epoch 14/50
900/900 [==============================] - 1s 871us/step - loss: 0.8897 - kullback_leibler_divergence: 0.8897 - acc: 0.7044 - val_loss: 1.7780 - val_kullback_leibler_divergence: 1.7780 - val_acc: 0.4400
Epoch 15/50
900/900 [==============================] - 1s 904us/step - loss: 0.8300 - kullback_leibler_divergence: 0.8300 - acc: 0.7256 - val_loss: 1.9861 - val_kullback_leibler_divergence: 1.9861 - val_acc: 0.3500
Epoch 16/50
900/900 [==============================] - 1s 906us/step - loss: 0.7779 - kullback_leibler_divergence: 0.7779 - acc: 0.7500 - val_loss: 1.7770 - val_kullback_leibler_divergence: 1.7770 - val_acc: 0.4600
Epoch 17/50
900/900 [==============================] - 1s 933us/step - loss: 0.6839 - kullback_leibler_divergence: 0.6839 - acc: 0.7889 - val_loss: 1.6734 - val_kullback_leibler_divergence: 1.6734 - val_acc: 0.4700
Epoch 18/50
900/900 [==============================] - 1s 910us/step - loss: 0.6113 - kullback_leibler_divergence: 0.6113 - acc: 0.8122 - val_loss: 1.8250 - val_kullback_leibler_divergence: 1.8250 - val_acc: 0.4300
Epoch 19/50
900/900 [==============================] - 1s 914us/step - loss: 0.5799 - kullback_leibler_divergence: 0.5799 - acc: 0.8189 - val_loss: 1.9630 - val_kullback_leibler_divergence: 1.9630 - val_acc: 0.4300
Epoch 20/50
900/900 [==============================] - 1s 903us/step - loss: 0.4977 - kullback_leibler_divergence: 0.4977 - acc: 0.8411 - val_loss: 1.9377 - val_kullback_leibler_divergence: 1.9377 - val_acc: 0.4400
Epoch 21/50
900/900 [==============================] - 1s 918us/step - loss: 0.4949 - kullback_leibler_divergence: 0.4949 - acc: 0.8467 - val_loss: 1.9478 - val_kullback_leibler_divergence: 1.9478 - val_acc: 0.4300
Epoch 22/50
900/900 [==============================] - 1s 1ms/step - loss: 0.4018 - kullback_leibler_divergence: 0.4018 - acc: 0.8833 - val_loss: 1.7994 - val_kullback_leibler_divergence: 1.7994 - val_acc: 0.5000
Epoch 23/50
900/900 [==============================] - 1s 934us/step - loss: 0.3695 - kullback_leibler_divergence: 0.3695 - acc: 0.9022 - val_loss: 1.9664 - val_kullback_leibler_divergence: 1.9664 - val_acc: 0.4500
Epoch 24/50
900/900 [==============================] - 1s 914us/step - loss: 0.3339 - kullback_leibler_divergence: 0.3339 - acc: 0.9044 - val_loss: 1.8579 - val_kullback_leibler_divergence: 1.8579 - val_acc: 0.4700
Epoch 25/50
900/900 [==============================] - 1s 900us/step - loss: 0.3003 - kullback_leibler_divergence: 0.3003 - acc: 0.9278 - val_loss: 2.0000 - val_kullback_leibler_divergence: 2.0000 - val_acc: 0.4500
Epoch 26/50
900/900 [==============================] - 1s 902us/step - loss: 0.2747 - kullback_leibler_divergence: 0.2747 - acc: 0.9289 - val_loss: 2.1076 - val_kullback_leibler_divergence: 2.1076 - val_acc: 0.4500
Epoch 27/50
900/900 [==============================] - 1s 916us/step - loss: 0.2611 - kullback_leibler_divergence: 0.2611 - acc: 0.9322 - val_loss: 1.9911 - val_kullback_leibler_divergence: 1.9911 - val_acc: 0.4800
Epoch 28/50
900/900 [==============================] - 1s 911us/step - loss: 0.2128 - kullback_leibler_divergence: 0.2128 - acc: 0.9511 - val_loss: 2.0426 - val_kullback_leibler_divergence: 2.0426 - val_acc: 0.4800
Epoch 29/50
900/900 [==============================] - 1s 932us/step - loss: 0.2019 - kullback_leibler_divergence: 0.2019 - acc: 0.9522 - val_loss: 2.0825 - val_kullback_leibler_divergence: 2.0825 - val_acc: 0.4700
Epoch 30/50
900/900 [==============================] - 1s 913us/step - loss: 0.2030 - kullback_leibler_divergence: 0.2030 - acc: 0.9456 - val_loss: 2.0270 - val_kullback_leibler_divergence: 2.0270 - val_acc: 0.4900
Epoch 31/50
900/900 [==============================] - 1s 897us/step - loss: 0.1588 - kullback_leibler_divergence: 0.1588 - acc: 0.9589 - val_loss: 2.4442 - val_kullback_leibler_divergence: 2.4442 - val_acc: 0.4500
Epoch 32/50
900/900 [==============================] - 1s 920us/step - loss: 0.1408 - kullback_leibler_divergence: 0.1408 - acc: 0.9667 - val_loss: 2.3015 - val_kullback_leibler_divergence: 2.3015 - val_acc: 0.4600
Epoch 33/50
900/900 [==============================] - 1s 927us/step - loss: 0.1225 - kullback_leibler_divergence: 0.1225 - acc: 0.9833 - val_loss: 2.1124 - val_kullback_leibler_divergence: 2.1124 - val_acc: 0.5100
Epoch 34/50
900/900 [==============================] - 1s 892us/step - loss: 0.1131 - kullback_leibler_divergence: 0.1131 - acc: 0.9833 - val_loss: 2.4244 - val_kullback_leibler_divergence: 2.4244 - val_acc: 0.4300
Epoch 35/50
900/900 [==============================] - 1s 915us/step - loss: 0.0997 - kullback_leibler_divergence: 0.0997 - acc: 0.9822 - val_loss: 2.2924 - val_kullback_leibler_divergence: 2.2924 - val_acc: 0.4900
Epoch 36/50
900/900 [==============================] - 1s 915us/step - loss: 0.0855 - kullback_leibler_divergence: 0.0855 - acc: 0.9878 - val_loss: 2.4548 - val_kullback_leibler_divergence: 2.4548 - val_acc: 0.5100
Epoch 37/50
900/900 [==============================] - 1s 928us/step - loss: 0.0799 - kullback_leibler_divergence: 0.0799 - acc: 0.9911 - val_loss: 2.5295 - val_kullback_leibler_divergence: 2.5295 - val_acc: 0.4600
Epoch 38/50
900/900 [==============================] - 1s 899us/step - loss: 0.0805 - kullback_leibler_divergence: 0.0805 - acc: 0.9889 - val_loss: 2.3695 - val_kullback_leibler_divergence: 2.3695 - val_acc: 0.5200
Epoch 39/50
900/900 [==============================] - 1s 906us/step - loss: 0.0824 - kullback_leibler_divergence: 0.0824 - acc: 0.9833 - val_loss: 2.4454 - val_kullback_leibler_divergence: 2.4454 - val_acc: 0.4900
Epoch 40/50
900/900 [==============================] - 1s 912us/step - loss: 0.0778 - kullback_leibler_divergence: 0.0778 - acc: 0.9889 - val_loss: 2.3969 - val_kullback_leibler_divergence: 2.3969 - val_acc: 0.5000
Epoch 41/50
900/900 [==============================] - 1s 927us/step - loss: 0.0666 - kullback_leibler_divergence: 0.0666 - acc: 0.9867 - val_loss: 2.4936 - val_kullback_leibler_divergence: 2.4936 - val_acc: 0.4600
Epoch 42/50
900/900 [==============================] - 1s 924us/step - loss: 0.0639 - kullback_leibler_divergence: 0.0639 - acc: 0.9900 - val_loss: 2.4973 - val_kullback_leibler_divergence: 2.4973 - val_acc: 0.4800
Epoch 43/50
900/900 [==============================] - 1s 911us/step - loss: 0.0643 - kullback_leibler_divergence: 0.0643 - acc: 0.9878 - val_loss: 2.6138 - val_kullback_leibler_divergence: 2.6138 - val_acc: 0.4600
Epoch 44/50
900/900 [==============================] - 1s 920us/step - loss: 0.0462 - kullback_leibler_divergence: 0.0462 - acc: 0.9944 - val_loss: 2.7283 - val_kullback_leibler_divergence: 2.7283 - val_acc: 0.4600
Epoch 45/50
900/900 [==============================] - 1s 913us/step - loss: 0.0439 - kullback_leibler_divergence: 0.0439 - acc: 0.9956 - val_loss: 2.6813 - val_kullback_leibler_divergence: 2.6813 - val_acc: 0.4800
Epoch 46/50
900/900 [==============================] - 1s 924us/step - loss: 0.0471 - kullback_leibler_divergence: 0.0471 - acc: 0.9911 - val_loss: 2.5326 - val_kullback_leibler_divergence: 2.5326 - val_acc: 0.5100
Epoch 47/50
900/900 [==============================] - 1s 910us/step - loss: 0.0401 - kullback_leibler_divergence: 0.0401 - acc: 0.9978 - val_loss: 2.7023 - val_kullback_leibler_divergence: 2.7023 - val_acc: 0.4500
Epoch 48/50
900/900 [==============================] - 1s 920us/step - loss: 0.0379 - kullback_leibler_divergence: 0.0379 - acc: 0.9956 - val_loss: 2.7047 - val_kullback_leibler_divergence: 2.7047 - val_acc: 0.4500
Epoch 49/50
900/900 [==============================] - 1s 911us/step - loss: 0.0393 - kullback_leibler_divergence: 0.0393 - acc: 0.9922 - val_loss: 2.5222 - val_kullback_leibler_divergence: 2.5222 - val_acc: 0.5200
Epoch 50/50
900/900 [==============================] - 1s 889us/step - loss: 0.0357 - kullback_leibler_divergence: 0.0357 - acc: 0.9956 - val_loss: 2.5932 - val_kullback_leibler_divergence: 2.5932 - val_acc: 0.4900
train data:
1000/1000 [==============================] - 0s 243us/step
kullback_leibler_divergence :  0.26798238860815765

acc :  0.949

test data:
10000/10000 [==============================] - 2s 240us/step
kullback_leibler_divergence :  2.733334423828125
acc :  0.4406
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ python3 imageBC.py 
Using TensorFlow backend.
WARNING: Logging before flag parsing goes to stderr.
W0626 21:31:05.130077 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:74: The name tf.get_default_graph is deprecated. Please use tf.compat.v1.get_default_graph instead.

W0626 21:31:05.141990 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:517: The name tf.placeholder is deprecated. Please use tf.compat.v1.placeholder instead.

W0626 21:31:05.143484 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:4138: The name tf.random_uniform is deprecated. Please use tf.random.uniform instead.

W0626 21:31:05.154716 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3976: The name tf.nn.max_pool is deprecated. Please use tf.nn.max_pool2d instead.

W0626 21:31:05.182251 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:133: The name tf.placeholder_with_default is deprecated. Please use tf.compat.v1.placeholder_with_default instead.

W0626 21:31:05.186783 4351911360 deprecation.py:506] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:3445: calling dropout (from tensorflow.python.ops.nn_ops) with keep_prob is deprecated and will be removed in a future version.
Instructions for updating:
Please use `rate` instead of `keep_prob`. Rate should be set to `rate = 1 - keep_prob`.
W0626 21:31:05.222163 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/optimizers.py:790: The name tf.train.Optimizer is deprecated. Please use tf.compat.v1.train.Optimizer instead.

W0626 21:31:05.227684 4351911360 deprecation_wrapper.py:119] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/keras/backend/tensorflow_backend.py:1521: The name tf.log is deprecated. Please use tf.math.log instead.

_________________________________________________________________
Layer (type)                 Output Shape              Param #   
=================================================================
conv2d_1 (Conv2D)            (None, 32, 32, 32)        896       
_________________________________________________________________
max_pooling2d_1 (MaxPooling2 (None, 16, 16, 32)        0         
_________________________________________________________________
conv2d_2 (Conv2D)            (None, 16, 16, 64)        18496     
_________________________________________________________________
max_pooling2d_2 (MaxPooling2 (None, 8, 8, 64)          0         
_________________________________________________________________
flatten_1 (Flatten)          (None, 4096)              0         
_________________________________________________________________
dense_1 (Dense)              (None, 512)               2097664   
_________________________________________________________________
dropout_1 (Dropout)          (None, 512)               0         
_________________________________________________________________
dense_2 (Dense)              (None, 10)                5130      
_________________________________________________________________
activation_1 (Activation)    (None, 10)                0         
=================================================================
Total params: 2,122,186
Trainable params: 2,122,186
Non-trainable params: 0
_________________________________________________________________
W0626 21:31:05.323875 4351911360 deprecation.py:323] From /Users/shoichi/Desktop/research_git/train1000-master/test/lib/python3.7/site-packages/tensorflow/python/ops/math_grad.py:1250: add_dispatch_support.<locals>.wrapper (from tensorflow.python.ops.array_ops) is deprecated and will be removed in a future version.
Instructions for updating:
Use tf.where in 2.0, which has the same broadcast rule as np.where
Train on 900 samples, validate on 100 samples
Epoch 1/50
2019-06-26 21:31:05.548267: I tensorflow/core/platform/cpu_feature_guard.cc:142] Your CPU supports instructions that this TensorFlow binary was not compiled to use: AVX2 FMA
900/900 [==============================] - 1s 1ms/step - loss: 2.1282 - kullback_leibler_divergence: 2.1282 - acc: 0.2311 - val_loss: 2.0868 - val_kullback_leibler_divergence: 2.0868 - val_acc: 0.2000
Epoch 2/50
900/900 [==============================] - 1s 881us/step - loss: 1.9111 - kullback_leibler_divergence: 1.9111 - acc: 0.3300 - val_loss: 1.9324 - val_kullback_leibler_divergence: 1.9324 - val_acc: 0.2600
Epoch 3/50
900/900 [==============================] - 1s 888us/step - loss: 1.7421 - kullback_leibler_divergence: 1.7421 - acc: 0.3933 - val_loss: 1.7957 - val_kullback_leibler_divergence: 1.7957 - val_acc: 0.3200
Epoch 4/50
900/900 [==============================] - 1s 918us/step - loss: 1.5606 - kullback_leibler_divergence: 1.5606 - acc: 0.4700 - val_loss: 1.7851 - val_kullback_leibler_divergence: 1.7851 - val_acc: 0.3200
Epoch 5/50
900/900 [==============================] - 1s 893us/step - loss: 1.4597 - kullback_leibler_divergence: 1.4597 - acc: 0.4867 - val_loss: 1.7114 - val_kullback_leibler_divergence: 1.7114 - val_acc: 0.3400
Epoch 6/50
900/900 [==============================] - 1s 902us/step - loss: 1.3560 - kullback_leibler_divergence: 1.3560 - acc: 0.5678 - val_loss: 1.6656 - val_kullback_leibler_divergence: 1.6656 - val_acc: 0.4200
Epoch 7/50
900/900 [==============================] - 1s 935us/step - loss: 1.2137 - kullback_leibler_divergence: 1.2137 - acc: 0.5889 - val_loss: 1.4291 - val_kullback_leibler_divergence: 1.4291 - val_acc: 0.5700
Epoch 8/50
900/900 [==============================] - 1s 878us/step - loss: 1.1403 - kullback_leibler_divergence: 1.1403 - acc: 0.6111 - val_loss: 1.6173 - val_kullback_leibler_divergence: 1.6173 - val_acc: 0.5000
Epoch 9/50
900/900 [==============================] - 1s 896us/step - loss: 1.0513 - kullback_leibler_divergence: 1.0513 - acc: 0.6389 - val_loss: 1.4772 - val_kullback_leibler_divergence: 1.4772 - val_acc: 0.5200
Epoch 10/50
900/900 [==============================] - 1s 900us/step - loss: 0.9321 - kullback_leibler_divergence: 0.9321 - acc: 0.7067 - val_loss: 1.5792 - val_kullback_leibler_divergence: 1.5792 - val_acc: 0.4300
Epoch 11/50
900/900 [==============================] - 1s 898us/step - loss: 0.8384 - kullback_leibler_divergence: 0.8384 - acc: 0.7278 - val_loss: 1.5566 - val_kullback_leibler_divergence: 1.5566 - val_acc: 0.4300
Epoch 12/50
900/900 [==============================] - 1s 904us/step - loss: 0.7016 - kullback_leibler_divergence: 0.7016 - acc: 0.7744 - val_loss: 1.4702 - val_kullback_leibler_divergence: 1.4702 - val_acc: 0.4800
Epoch 13/50
900/900 [==============================] - 1s 924us/step - loss: 0.6517 - kullback_leibler_divergence: 0.6517 - acc: 0.8022 - val_loss: 1.7190 - val_kullback_leibler_divergence: 1.7190 - val_acc: 0.4300
Epoch 14/50
900/900 [==============================] - 1s 892us/step - loss: 0.5688 - kullback_leibler_divergence: 0.5688 - acc: 0.8422 - val_loss: 1.6896 - val_kullback_leibler_divergence: 1.6896 - val_acc: 0.3900
Epoch 15/50
900/900 [==============================] - 1s 890us/step - loss: 0.5019 - kullback_leibler_divergence: 0.5019 - acc: 0.8589 - val_loss: 1.7911 - val_kullback_leibler_divergence: 1.7911 - val_acc: 0.3800
Epoch 16/50
900/900 [==============================] - 1s 892us/step - loss: 0.4426 - kullback_leibler_divergence: 0.4426 - acc: 0.8756 - val_loss: 1.5687 - val_kullback_leibler_divergence: 1.5687 - val_acc: 0.4900
Epoch 17/50
900/900 [==============================] - 1s 919us/step - loss: 0.4013 - kullback_leibler_divergence: 0.4013 - acc: 0.8933 - val_loss: 1.7597 - val_kullback_leibler_divergence: 1.7597 - val_acc: 0.4600
Epoch 18/50
900/900 [==============================] - 1s 904us/step - loss: 0.3529 - kullback_leibler_divergence: 0.3529 - acc: 0.9078 - val_loss: 1.9959 - val_kullback_leibler_divergence: 1.9959 - val_acc: 0.3900
Epoch 19/50
900/900 [==============================] - 1s 897us/step - loss: 0.3101 - kullback_leibler_divergence: 0.3101 - acc: 0.9200 - val_loss: 1.9306 - val_kullback_leibler_divergence: 1.9306 - val_acc: 0.4600
Epoch 20/50
900/900 [==============================] - 1s 909us/step - loss: 0.2564 - kullback_leibler_divergence: 0.2564 - acc: 0.9356 - val_loss: 1.9927 - val_kullback_leibler_divergence: 1.9927 - val_acc: 0.4400
Epoch 21/50
900/900 [==============================] - 1s 917us/step - loss: 0.2238 - kullback_leibler_divergence: 0.2238 - acc: 0.9367 - val_loss: 2.1204 - val_kullback_leibler_divergence: 2.1204 - val_acc: 0.4200
Epoch 22/50
900/900 [==============================] - 1s 926us/step - loss: 0.2172 - kullback_leibler_divergence: 0.2172 - acc: 0.9467 - val_loss: 2.0064 - val_kullback_leibler_divergence: 2.0064 - val_acc: 0.4800
Epoch 23/50
900/900 [==============================] - 1s 899us/step - loss: 0.1878 - kullback_leibler_divergence: 0.1878 - acc: 0.9578 - val_loss: 2.0511 - val_kullback_leibler_divergence: 2.0511 - val_acc: 0.4400
Epoch 24/50
900/900 [==============================] - 1s 901us/step - loss: 0.1783 - kullback_leibler_divergence: 0.1783 - acc: 0.9522 - val_loss: 1.8829 - val_kullback_leibler_divergence: 1.8829 - val_acc: 0.4600
Epoch 25/50
900/900 [==============================] - 1s 896us/step - loss: 0.1331 - kullback_leibler_divergence: 0.1331 - acc: 0.9689 - val_loss: 2.1022 - val_kullback_leibler_divergence: 2.1022 - val_acc: 0.5000
Epoch 26/50
900/900 [==============================] - 1s 891us/step - loss: 0.1206 - kullback_leibler_divergence: 0.1206 - acc: 0.9744 - val_loss: 2.1909 - val_kullback_leibler_divergence: 2.1909 - val_acc: 0.4600
Epoch 27/50
900/900 [==============================] - 1s 902us/step - loss: 0.1226 - kullback_leibler_divergence: 0.1226 - acc: 0.9733 - val_loss: 2.1652 - val_kullback_leibler_divergence: 2.1652 - val_acc: 0.4400
Epoch 28/50
900/900 [==============================] - 1s 892us/step - loss: 0.0986 - kullback_leibler_divergence: 0.0986 - acc: 0.9833 - val_loss: 2.2177 - val_kullback_leibler_divergence: 2.2177 - val_acc: 0.4300
Epoch 29/50
900/900 [==============================] - 1s 903us/step - loss: 0.0836 - kullback_leibler_divergence: 0.0836 - acc: 0.9867 - val_loss: 2.1734 - val_kullback_leibler_divergence: 2.1734 - val_acc: 0.4800
Epoch 30/50
900/900 [==============================] - 1s 900us/step - loss: 0.0704 - kullback_leibler_divergence: 0.0704 - acc: 0.9911 - val_loss: 2.3617 - val_kullback_leibler_divergence: 2.3617 - val_acc: 0.4500
Epoch 31/50
900/900 [==============================] - 1s 920us/step - loss: 0.0580 - kullback_leibler_divergence: 0.0580 - acc: 0.9900 - val_loss: 2.3310 - val_kullback_leibler_divergence: 2.3310 - val_acc: 0.5100
Epoch 32/50
900/900 [==============================] - 1s 908us/step - loss: 0.0600 - kullback_leibler_divergence: 0.0600 - acc: 0.9900 - val_loss: 2.4825 - val_kullback_leibler_divergence: 2.4825 - val_acc: 0.4300
Epoch 33/50
900/900 [==============================] - 1s 912us/step - loss: 0.0586 - kullback_leibler_divergence: 0.0586 - acc: 0.9922 - val_loss: 2.4984 - val_kullback_leibler_divergence: 2.4984 - val_acc: 0.4200
Epoch 34/50
900/900 [==============================] - 1s 930us/step - loss: 0.0485 - kullback_leibler_divergence: 0.0485 - acc: 0.9944 - val_loss: 2.3601 - val_kullback_leibler_divergence: 2.3601 - val_acc: 0.4300
Epoch 35/50
900/900 [==============================] - 1s 904us/step - loss: 0.0363 - kullback_leibler_divergence: 0.0363 - acc: 0.9978 - val_loss: 2.3872 - val_kullback_leibler_divergence: 2.3872 - val_acc: 0.4800
Epoch 36/50
900/900 [==============================] - 1s 887us/step - loss: 0.0423 - kullback_leibler_divergence: 0.0423 - acc: 0.9956 - val_loss: 2.5182 - val_kullback_leibler_divergence: 2.5182 - val_acc: 0.4100
Epoch 37/50
900/900 [==============================] - 1s 926us/step - loss: 0.0451 - kullback_leibler_divergence: 0.0451 - acc: 0.9911 - val_loss: 2.5012 - val_kullback_leibler_divergence: 2.5012 - val_acc: 0.4700
Epoch 38/50
900/900 [==============================] - 1s 902us/step - loss: 0.0419 - kullback_leibler_divergence: 0.0419 - acc: 0.9944 - val_loss: 2.5486 - val_kullback_leibler_divergence: 2.5486 - val_acc: 0.4500
Epoch 39/50
900/900 [==============================] - 1s 900us/step - loss: 0.0387 - kullback_leibler_divergence: 0.0387 - acc: 0.9944 - val_loss: 2.3781 - val_kullback_leibler_divergence: 2.3781 - val_acc: 0.5200
Epoch 40/50
900/900 [==============================] - 1s 898us/step - loss: 0.0379 - kullback_leibler_divergence: 0.0379 - acc: 0.9944 - val_loss: 2.3985 - val_kullback_leibler_divergence: 2.3985 - val_acc: 0.5100
Epoch 41/50
900/900 [==============================] - 1s 897us/step - loss: 0.0279 - kullback_leibler_divergence: 0.0279 - acc: 0.9989 - val_loss: 2.7751 - val_kullback_leibler_divergence: 2.7751 - val_acc: 0.4000
Epoch 42/50
900/900 [==============================] - 1s 889us/step - loss: 0.0271 - kullback_leibler_divergence: 0.0271 - acc: 0.9978 - val_loss: 2.6707 - val_kullback_leibler_divergence: 2.6707 - val_acc: 0.5400
Epoch 43/50
900/900 [==============================] - 1s 895us/step - loss: 0.0214 - kullback_leibler_divergence: 0.0214 - acc: 0.9989 - val_loss: 2.6228 - val_kullback_leibler_divergence: 2.6228 - val_acc: 0.5300
Epoch 44/50
900/900 [==============================] - 1s 943us/step - loss: 0.0175 - kullback_leibler_divergence: 0.0175 - acc: 1.0000 - val_loss: 2.7691 - val_kullback_leibler_divergence: 2.7691 - val_acc: 0.4800
Epoch 45/50
900/900 [==============================] - 1s 906us/step - loss: 0.0184 - kullback_leibler_divergence: 0.0184 - acc: 0.9989 - val_loss: 2.8120 - val_kullback_leibler_divergence: 2.8120 - val_acc: 0.4800
Epoch 46/50
900/900 [==============================] - 1s 908us/step - loss: 0.0187 - kullback_leibler_divergence: 0.0187 - acc: 0.9989 - val_loss: 2.8677 - val_kullback_leibler_divergence: 2.8677 - val_acc: 0.5000
Epoch 47/50
900/900 [==============================] - 1s 935us/step - loss: 0.0154 - kullback_leibler_divergence: 0.0154 - acc: 1.0000 - val_loss: 2.7084 - val_kullback_leibler_divergence: 2.7084 - val_acc: 0.5400
Epoch 48/50
900/900 [==============================] - 1s 906us/step - loss: 0.0161 - kullback_leibler_divergence: 0.0161 - acc: 1.0000 - val_loss: 2.7426 - val_kullback_leibler_divergence: 2.7426 - val_acc: 0.5100
Epoch 49/50
900/900 [==============================] - 1s 914us/step - loss: 0.0147 - kullback_leibler_divergence: 0.0147 - acc: 0.9967 - val_loss: 2.9023 - val_kullback_leibler_divergence: 2.9023 - val_acc: 0.5000
Epoch 50/50
900/900 [==============================] - 1s 899us/step - loss: 0.0167 - kullback_leibler_divergence: 0.0167 - acc: 0.9989 - val_loss: 3.0352 - val_kullback_leibler_divergence: 3.0352 - val_acc: 0.4900
train data:
1000/1000 [==============================] - 0s 243us/step
kullback_leibler_divergence :  0.30605134851671756

acc :  0.949

test data:
10000/10000 [==============================] - 2s 249us/step
kullback_leibler_divergence :  3.911144497680664
acc :  0.365
(test) YaCnoMacBook-puro:train1000-master shoichi$ ls
README.md		c.png			e.png			sample			sample_cifar10.py	test			wig_ensemble_cifar.py
WiG			d.png			get_models.sh		sample1.png		sample_cifar100.py	train1000.py		wig_ensemble_mnist.py
__pycache__		data.py			imageBC.py		sample2.png		sample_mnist.csv	trainwith1000result.txt
a.png			demon1.png		my1000sample.py		sample_cifar10.csv	sample_mnist.hdf5	untitled2.py
b.png			demon2.png		myTrainwith1000.py	sample_cifar10.hdf5	sample_mnist.py		untitled4.py
(test) YaCnoMacBook-puro:train1000-master shoichi$ 
(test) YaCnoMacBook-puro:train1000-master shoichi$ vim imageBC.py

    model.add(Flatten())
    model.add(Dense(512, activation="relu"))
    model.add(Dropout(0.5))
    model.add(Dense(10))                                              #全結合2層目
    model.add(Activation("softmax"))
    model.compile(loss='kullback_leibler_divergence', optimizer=Adam(), metrics=['kullback_leibler_divergence', 'acc'])
    
    model.summary()
    return model

def BClearning_generator(X_train,Y_train):
    label = np.argmax(Y_train,axis=1)
    for i in range(X_train.shape[0] -1 ):
        if(label[i+1] < label[i]):
            temp = X_train[i]
            X_train[i] = X_train[i+1]
            X_train[i+1] = temp
            temp2 = Y_train[i]
            Y_train[i] = Y_train[i+1]
            Y_train[i+1] = temp2
    
    #5クラスずつにソート半分ずつに分ける500,500
    sub_X_train1 , sub_X_train2 = np.array_split(X_train,2)
    #各ラベルのXをと、各ラベル+5のXをweight（0.1,0.9）をかけあう
    for i in range(len(sub_X_train1) -1 ):
        np.append(X_train,cv2.addWeighted(X_train[i],0.3,sub_X_train2[i],0.7,0))
        np.append(X_train,cv2.addWeighted(X_train[i+500],0.7,sub_X_train1[i],0.3,0))
    return X_train,Y_train


if __name__ == '__main__':
    (X_train,Y_train),(X_test,Y_test) = train1000.cifar10()
    X_train,Y_train = BClearning_generator(X_train,Y_train)

    epochs = 50
    batch_size = 100
    nb_classes = 10
    model = model()
    result = model.fit(X_train, Y_train, batch_size=batch_size, epochs=epochs, validation_split=0.1,verbose=1)

    print('train data:')
    eva=model.evaluate(X_train,Y_train,verbose=1)
    for i in range(1,len(model.metrics_names)):
        print( model.metrics_names[i] + ' : ', eva[i] )
        print()

    print('test data:')
    eva = model.evaluate(X_test,Y_test,verbose=1)
    for i in range(1,len(model.metrics_names)):
        print( model.metrics_names[i] + ' : ', eva[i] )

