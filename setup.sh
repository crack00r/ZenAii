echo "First, Create a telegram account..."

echo "...And Then... Go here and get an API key and hash under Dev Tools: https://my.telegram.org/auth"

sudo apt install -y build-essential
sudo curl -sL https://deb.nodesource.com/setup_7.x | sudo -E bash -
sudo apt-get install -y nodejs nodejs-legacy mongodb
sudo npm install
sudo npm link
sudo apt install python3 python3-pip
sudo python3 setup.py gen_tl
sudo python3 setup.py install

echo "...And Then... Input your hash and key and phone into explorer.py..."

echo "...And Then... Edit npm_modules/poloniex.js/lib.poloniex.js and set sslstrict to false for speed"

echo "...And Then... Sign up for cruptoping and link your telegram account to it... Wait for the signals brother."

echo "...And Then... sudo python3 trader.py"



