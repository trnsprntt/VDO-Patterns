package tests;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class V_219165 {

	public static void main(String[] args) {
	    
	    String v_219165 = "grep pam_lastlog /etc/pam.d/login";

	    ExecuteShellComand obj = new V_219165();
		
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
				output.append(line + "\n");
			}

		} catch (Exception e) {
			e.printStackTrace();
		}

		return output.toString();

	}

}
