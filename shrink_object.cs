using System;
using System.Drawing;
using System.Drawing.Drawing2D;
using System.IO;

class Program {
    static void Main(string[] args) {
        string inputFile = args[0];
        string outputFile = args[1];
        float scale = 0.8f;
        
        using (Bitmap orig = new Bitmap(inputFile)) {
            int nw = (int)(orig.Width * scale);
            int nh = (int)(orig.Height * scale);
            
            using (Bitmap scaled = new Bitmap(orig, nw, nh))
            using (Graphics gs = Graphics.FromImage(scaled)) {
                gs.InterpolationMode = InterpolationMode.HighQualityBicubic;
                gs.DrawImage(orig, 0, 0, nw, nh);
            
                using (Bitmap final = new Bitmap(orig.Width, orig.Height))
                using (Graphics g = Graphics.FromImage(final)) {
                    Color bgColor = orig.GetPixel(0, 0); // top-left edge pixel
                    g.Clear(bgColor);
                    
                    int x = (orig.Width - nw) / 2;
                    int y = (orig.Height - nh) / 2;
                    g.DrawImage(scaled, x, y);
                    
                    final.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
                }
            }
        }
    }
}
