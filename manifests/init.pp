Exec { path => [ "/bin/", "/sbin/" , "/usr/bin/", "/usr/sbin/" ] }

class core {
  
    exec { "apt-update":
      command => "/usr/bin/sudo apt-get -y update"
    }
  
    package { 
      [ "vim", "git-core", "build-essential" ]:
        ensure => ["installed"],
        require => Exec['apt-update']    
    }
}

class python {

    package { 
      [ "python", "python-setuptools", "python-dev", "python-pip", ]:
        ensure => ["installed"],
        require => Exec['apt-update']    
    }

    exec {
      "virtualenv":
      command => "/usr/bin/sudo pip install virtualenv",
      require => Package["python-dev", "python-pip"]
    }

}

class networking {
    package { 
      [ "snmp", "tkmib", "curl", "wget" ]:
        ensure => ["installed"],
        require => Exec['apt-update']    
    }
    
}

class web {

    exec {
      "django":
      command => "/usr/bin/sudo pip install django",
      require => Package["python-pip"],
      onlyif => "pip freeze | grep django != ''",
    }
    
    #web server
    exec {
      "gunicorn":
      command => "/usr/bin/sudo pip install gunicorn",
      require => Package["python-pip"],
      onlyif => "pip freeze | grep unicorn != ''",
    }
    
    # static file handler
    exec {
      "whitenoise":
      command => "/usr/bin/sudo pip install whitenoise",
      require => Package["python-pip"],
      onlyif => "pip freeze | grep whitenoise != ''",
    }
    
    exec {
        "heroku-toolbelt":
        command => "wget -qO- https://toolbelt.heroku.com/install-ubuntu.sh | sh",
        creates => "/usr/local/heroku",
        require =>Package["wget"],  
    }
}

class mysql {
  package {
    ["mysql-client-core-5.5","mysql-client", "mysql-server", "libmysqlclient-dev"]: 
      ensure => installed, 
      require => Exec['apt-update']
  }
  
  service { "mysql":
    ensure    => running,
    enable    => true,
    require => Package["mysql-server"],  
  }
}

include core
include python
include networking
include web
include mysql