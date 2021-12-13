from os import listdir
from os import makedirs
from os import path
from os import chdir
from os.path import isfile, join
requirements_folder = "requirements"
tests_folder = "src/tests/"
requirements = [f for f in listdir(requirements_folder) if isfile(join(requirements_folder, f))]
for r in requirements:
    with open(requirements_folder +"/"+ r, 'r') as f:
        requirement = f.read()
        if requirement.find("V-219165")!=-1:
            test = '''import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;
import java.io.*;

public class V219165 {

    public static void main(String[] args) {
        
        String v_219165 = "grep pam_lastlog /etc/pam.d/login";

        V219165 obj = new V219165();
        
        String file_content = obj.executeCommand("cat /etc/pam.d/login");
        
        System.out.println(file_content);
        
        String output = obj.executeCommand(v_219165);

        assert (output == "" || !output.contains("required") || output.contains("silent")) == false;
    }

    private String executeCommand(String command) {

        StringBuffer output = new StringBuffer();

        Process p;
        try {
            p = Runtime.getRuntime().exec(command);
            p.waitFor();
            BufferedReader reader = 
                        new BufferedReader(new InputStreamReader(p.getInputStream()));

            String line = "";			
            while ((line = reader.readLine())!= null) {
                output.append(line + "\\n");
            }

        } catch (Exception e) {
            e.printStackTrace();
        }

        return output.toString();

    }

}'''
        elif requirement.find("")!=-1:
            test = '''some other text'''
    test_filename = tests_folder+r.replace(".txt","").replace('-','')+".java"
    # chdir("../")
    makedirs(path.dirname(test_filename), exist_ok=True)
    with open(test_filename, "w+") as out:
        out.write(test)
