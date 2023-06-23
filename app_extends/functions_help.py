import os;
import cv2;


def checkFingerPrintMatchV1(original_img_folder, sample):
    #p_img_path = "SOCOFing/Altered/Altered-Hard/2__F_Left_index_finger_CR.BMP";
    #p_img_path = suspected_img_path;
    #sample = cv2.imread(fp_img_path);
    
    '''
    cv2.imshow("Sample", sample);
    cv2.waitKey(0);
    cv2.destroyAllWindows();
    '''
    
    best_maching_score = 0;
    filename = None;
    image = None;
    kp_orig, kp_samp, mp = None, None, None;
    
    counter = 0;
    #original_img_folder = "SOCOFing/Real";
    #original_img_folder = "SOCOFing/Real";
    for file in [file for file in os.listdir(original_img_folder)]:#[:50]: #I want to check in the first 50 images
    
        #if 1 == 1: #counter % 10 == 0:
        if counter % 10 == 0:
            print(counter);
            print(file);
        counter += 1;
    
        fingerprint_image = cv2.imread(original_img_folder + "/" + file);
    
        #Scale invariant Feature Transform (SIFT), allows to extract the key points in the images
        sift = cv2.SIFT_create();   #Create sift object
    
        keypoints_1, descriptors_1 = sift.detectAndCompute(sample, None); #extracting the keypoints of sample image
        keypoints_2, descriptors_2 = sift.detectAndCompute(fingerprint_image, None); #extracting keypoints of the original images
    
        #For these keypoints, let's find the matches
        #Flann: Fast Library for Approximate Nearest Neighbors
        matches = cv2.FlannBasedMatcher({'algorithm':1, 'trees':10},
                {}).knnMatch(descriptors_1, descriptors_2, k=2); #k : the number of nearest neighbors
    
        #Let's try to find the releavent matches.
        match_points = [];
    
        for p, q in matches: #macthing 1:p , maching 2:q
            if p.distance < 0.1 * q.distance:
                match_points.append(p);
    
    
        keypoints = 0;
        if len(keypoints_1) < len(keypoints_2):
            keypoints = len(keypoints_1);
        else:
            keypoints = len(keypoints_2);
    
        if len(match_points) / keypoints * 100 > best_maching_score:
            best_score = len(match_points) / keypoints * 100;
            filename = file;
            image = fingerprint_image;
            kp_orig, kp_samp, mp = keypoints_1, keypoints_2, match_points;
    
    if filename == None:
        return None;
        pass;
    else:
        print("Best Match : "+str(filename));
        print("Score : "+str(best_score));
        result = cv2.drawMatches(sample,  kp_orig, image, kp_samp, mp, None);
        result = cv2.resize(result, None, fx=4, fy=4);
        cv2.imshow("Result ", result); 
        cv2.waitKey(0);
        cv2.destroyAllWindows();
        resultat = {};

        resultat['filename'] = filename;
        resultat['score'] = best_score;
        return resultat;
        pass;


