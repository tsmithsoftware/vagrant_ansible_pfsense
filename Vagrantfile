# -*- mode: ruby -*-
# vi: set ft=ruby :
servers=[
  { # root/opnsense
    :hostname => "web",
    :ip => "192.168.56.10",
    :box => "rudibroekhuizen/opnsense",
    :ram => 1024,
    :cpu => 2
  },
  {
    :hostname => "db",
    :ip => "192.168.56.11",
    :box => "rudibroekhuizen/opnsense",
    :ram => 1024,
    :cpu => 2
  }
]

Vagrant.configure("2") do |config|
	config.vm.provider "virtualbox" do |v|
	  v.check_guest_additions = false
	end
    servers.each do |machine|
        config.vm.define machine[:hostname] do |node|
		    node.vm.box_check_update = false
            node.vm.box = machine[:box]
			config.vm.network "public_network", ip: machine[:ip]
			config.vm.synced_folder '.', '/vagrant', disabled: true
            node.vm.provider "virtualbox" do |vb|
                vb.customize ["modifyvm", :id, "--memory", machine[:ram]]
            end
	    node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/my_key.pub"
	    node.vm.provision "shell", inline: <<-SHELL
		  cat ~/.ssh/my_key.pub >> ~/.ssh/authorized_keys
	    SHELL
        end
    end
end
