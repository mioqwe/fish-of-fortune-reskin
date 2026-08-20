## **Part 1: HTML Game Reskin**

### **Objective**

Reskin a [simple HTML game](https://drive.google.com/file/d/192vseQ7p3VVmw_PSNv01E4mqgI-Nep_Y/view?usp=sharing) so that it fits the aesthetic of “Fish of Fortune.” ([Android](https://play.google.com/store/apps/details?id=com.whalo.games.fishoffortune&hl=en) / [IOS](https://apps.apple.com/us/app/fish-of-fortune-go-fishing/id1608173176)) 

### **Requirements**

* **Base Code:** You will be provided with a [simple HTML game.](https://drive.google.com/file/d/192vseQ7p3VVmw_PSNv01E4mqgI-Nep_Y/view?usp=sharing)  
* **Tools:**  
  * **Visual Studio Code:** Use [Visual Studio code](https://code.visualstudio.com/) to work on the project.  
  * **Coding Agents:**  
    * **Cline for VS code:** Integrate [Cline](https://marketplace.visualstudio.com/items?itemName=saoudrizwan.claude-dev) and use [OpenRouter](https://openrouter.ai/) key as it is free. The models that you can use for code modification are listed below (you are free to use other models if you see fit):  
      * google/gemini-2.0-pro-exp-02-05:free  
      * deepseek/deepseek-r1:free  
    * [**Gemini Code Assist for VScode**](https://cloud.google.com/gemini/docs/codeassist/gemini-cli)  
    * [**Gemini CLI**](https://github.com/google-gemini/gemini-cli) **(run in a terminal inside VScode terminal)**  
    * **Copilot in VScode**  
    * [**Qwen coder**](https://chat.qwen.ai/)   
    * **Or any coding agent/tool based AI**  
        
* **Workflow:**  
  *  Enhance the game by utilizing AI coding agent to modify the visuals and incorporate any other necessary elements.   
  * You can tweak the code manually for the small adjustments after Cline did code modifications.   
      
* **Art Direction:** Change the game's visual appearance to match the world of Fish of Fortune. Enhance the look with:  
  * Custom reskin elements (backgrounds, sprites, UI components)  
  * Particle effects and any additional visual effects that boost the “amazing” and immersive feel  
  * Any other elements that will enhance the UX  
      
* **Technical:**   
  * Ensure all assets are compressed to the smallest possible file size.  
  * Use Gen-Ai models as the start of your visual enhancement  
      
* **Documentation:**  
  * Record / document every step of your process.  
  * Export your coding agent AI tasks into text files.  
  * Write down **only your time** on the project, not computer time.  
      
* **Deliverables:** Reskin folder with:  
  * **Game Folder** \- A folder containing the updated HTML game, all necessary assets (images, audio files, etc.), and any supporting files so that the game can be run locally from a single folder.  
  * **Source Folder** \- A folder with all the original source files. This includes PSDs, initial image generations, and any other relevant files created for this project.  
  * **A text file** (e.g., README.txt/PDF ) detailing your workflow, including the sources used and how you implemented Cline tasks.  
    

---

## **Part 2: 3D Models Creation**

### **Objective**

Create three optimized 3D models (in GLB format) that are “game ready” with low-poly count and optimized textures.

### **Workflow \- Generative AI Pipeline:**

1. **2D Concept:** Use a generative AI tool to create a 2D image that will serve as the foundation for the 3D model.  
2. **3D Conversion:** Convert the 2D concept into a 3D model using your preferred techniques or tools.  
3. **Optimization:** Ensure the resulting GLB model is optimized for real-time game performance by keeping polygon counts and texture sizes low. Add skin and rigging if necessary, but prioritize keeping the model lightweight.

### **Models to Create**

1. **Fish Model:**  
   * Style: In the style of Fish of Fortune.  
2. **Farm House Model:**  
   * Style: Reflecting the aesthetic of [Klondike Adventure commercials.](https://www.facebook.com/ads/library/?active_status=active&ad_type=all&country=ALL&is_targeted_country=false&media_type=all&search_type=page&view_all_page_id=451256781884275)  
3. **Character Model:**  
   * Requirements: A cute humanoid character featuring a Mixamo dancing animation.  
   * Animation: Ensure the exported GLB supports the animation in a game-ready format.

**Deliverables**

* **GLB folder \-** containing a folder per model with**:**  
  * Model and texture  
  * Any other files that were generated along the way (a folder for each model files)  
  * Text file with prompts used to generate assets and workflow summary

---

## **Submission Guidelines**

* **Packaging:**  
   Package your work into one ZIP file containing 2 folders:  
  * The reskinned HTML game folder.  
  * The GLB folder   
* **Documentation:**  
   Your README (or similarly named text file) should include:  
  * An explanation of your creative and technical approach.  
  * A list of all assets, sources, and external tools used.  
  * Detailed notes on how you implemented the Cline tasks.  
  * Any challenges encountered and how you resolved them.  
* **Execution:**  
   The HTML game should run locally from a single folder. All GLB models must be optimized and ready to be integrated into a game environment.

