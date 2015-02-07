Vagrant.configure("2") do |config|
  config.vm.box     = 'ubuntu/trusty64'

  #network
  config.vm.network :private_network, ip: "192.168.33.11"

  #shared
  config.vm.synced_folder "./projects", "/projects"

  #virtualbox
  if defined? VagrantVbguest
    config.vbguest.auto_update = true
  end
  config.vm.provider :virtualbox do |vb|
    vb.customize ["modifyvm", :id, "--natdnshostresolver1", "on"]
    vb.customize ["modifyvm", :id, "--memory", "512"]
  end

  config.vm.provision :puppet do |puppet|
    puppet.manifests_path = "manifests"
    puppet.manifest_file  = "init.pp"
    #puppet.module_path = "modules"
    #puppet.options = "--verbose --debug"
    #puppet.options = "--verbose --noop"
  end
  
  if Vagrant.has_plugin?("vagrant-cachier")
    # Configure cached packages to be shared between instances of the same base box.
    # More info on http://fgrehm.viewdocs.io/vagrant-cachier/usage
    config.cache.scope = :box

    # For more information please check http://docs.vagrantup.com/v2/synced-folders/basic_usage.html
  end
end