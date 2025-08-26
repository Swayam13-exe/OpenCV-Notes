import cv2
import numpy as np
src = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img6.jpg", 0)
template = cv2.imread("C:/Users/swayam/Desktop/DIVP/Images/img30.jpg", 0)
def hist_match(source, template):
    oldshape = source.shape
    source = source.ravel()
    template = template.ravel()
    s_values, bin_idx, s_counts = np.unique(source, return_inverse=True, return_counts=True)
    t_values, t_counts = np.unique(template, return_counts=True)
    s_quantiles = np.cumsum(s_counts).astype(np.float64) / source.size
    t_quantiles = np.cumsum(t_counts).astype(np.float64) / template.size
    interp_t_values = np.interp(s_quantiles, t_quantiles, t_values)
    return interp_t_values[bin_idx].reshape(oldshape).astype(np.uint8)
matched = hist_match(src, template)
cv2.imshow("Source img6", src)
cv2.imshow("Histogram Matched", matched)
key=cv2.waitKey(0)
if (key==97):
    cv2.destroyAllWindows()