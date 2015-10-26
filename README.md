#VagrantForSphinx

SphinxページをビルドするためのVagrant仮想マシン設定

### 環境

Ubuntu12.04:[hashicorp/precise64](https://vagrantcloud.com/hashicorp/precise64)
をベースに、以下の追加パッケージで構築

- make
- pip(python-pip)

- [Sphinx](http://sphinx-users.jp/)
- [sphinxtogithub](https://pypi.python.org/pypi/sphinxtogithub/1.0.0)
- [sphinx-bootstrap-theme](http://ryan-roemer.github.io/sphinx-bootstrap-theme/index.html)

### Prepare

- Pythonインストール
- fabricインストール

```
$ pip install fabric
```

- Vagrantインストール
- vagrant-fabric pluginインストール

```
$ vagrant plugin install vagrant-fabric
```

- git clone & vagrant up

```
$ git clone git@github.com:ryosms/VagrantForSphinx.git
$ cd VagrantForSphinx
$ vagrant up --provision
```

### USAGE

- build with fabric

```
$ fab make:/your/sphinx/path
or
$ fab clean_make:/your/sphinx/path
```

- clean with fabric

```
$ fab clean:/your/sphinx/path
```