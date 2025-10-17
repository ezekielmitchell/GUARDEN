from roboflow import Roboflow
import os

def test_roboflow_connection():
    try:
        # Initialize Roboflow (replace with your API key)
        rf = Roboflow(api_key="<<API KEY>>")
        print("✅ Successfully connected to Roboflow")
        
        # List available projects (this is a more basic API call)
        try:
            project = rf.workspace().project("example-project")
            print("✅ Successfully made API call to Roboflow")
            return True
        except Exception as e:
            if "Project not found" in str(e):
                print("✅ Successfully made API call to Roboflow (project not found is expected)")
                return True
            else:
                raise e
            
    except Exception as e:
        print("❌ Error connecting to Roboflow:")
        print(str(e))
        return False

if __name__ == "__main__":
    print("Testing Roboflow Connection...")
    test_roboflow_connection()