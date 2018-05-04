# Pyenvのインストール
```
brew install pyenv
```

.zshrcや.bashrc
```
export PYENV_ROOT="$HOME/.pyenv"
export PATH="$PYENV_ROOT/bin:$PATH"
eval "$(pyenv init -)"
```

# Pipenvインストール
```
brew install pipenv
```
pip経由でもインストールできます。
```
pip install pipenv
```

# PyenvでのPythonのインストール
```
pyenv install 3.6.5
pyenv global 3.6.5
```

本番環境
```
pipenv install
```
開発環境
```
pipenv install --dev
```


設定
Pipenvのコマンドはシェルで補完できます。
.bashrc .zshrc
```
eval "$(pipenv --completion)"
```

## ローカル起動
```
pipenv run start
```

## Dockerから起動
```
docker build -t flask_docker .
docker run -p 5000:5000 -it lask_docker
```
## 疎通
```
curl http://localhost:5000/reply -X POST -H "Content-Type: application/json" -d '{"keyword": "Keffia"}'
```
