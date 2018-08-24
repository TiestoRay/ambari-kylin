import os
import base64
from time import sleep
from resource_management import *

class NginxMaster(Script):
    def install(self, env):      
        import params
        self.install_packages(env)
        Directory([params.nginx_install_dir],
              mode=0755,
              cd_access='a',
              create_parents=True
        )
        Execute('cd ' + params.nginx_install_dir + '; wget ' + params.nginx_download_path + ' -O nginx.tar.gz  ')
        Execute('cd ' + params.nginx_install_dir + '; tar -xvf nginx.tar.gz')
        Execute('cd ' + params.nginx_install_dir + '; rm -rf latest; ln -s nginx latest')

    def configure(self, env):  
        import params
        env.set_params(params)
        File(format(params.nginx_install_dir + "/latest/conf/nginx.conf"), content=InlineTemplate(params.nginx_conf))
             
    def start(self, env):
        import params
        env.set_params(params)
        self.configure(env)
        Execute('cd ' + params.nginx_install_dir + "/latest; sbin/nginx")
        

    def stop(self, env):
        Execute("pkill -9 nginx")


    def restart(self, env):
        import params
        Execute('cd ' + params.nginx_install_dir + "/latest; sbin/nginx -s reload")

    def status(self, env):
        check_process_status("/var/run/nginx.pid")


if __name__ == "__main__":
    NginxMaster().execute()
