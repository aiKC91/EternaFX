import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

class BodyScannerVisualizer:
    @staticmethod
    def visualize_scan(scan_data):
        """
        3D scatter plot of the scanned data for real-time insights.
        """
        if scan_data is None:
            print("No body scan data to visualize.")
            return
        
        fig = plt.figure()
        ax = fig.add_subplot(111, projection="3d")
        ax.scatter(scan_data[:,0], scan_data[:,1], scan_data[:,2], c='blue', marker='o')
        ax.set_xlabel("X")
        ax.set_ylabel("Y")
        ax.set_zlabel("Z")
        ax.set_title("3D Body Scanner Visualization")
        plt.show()