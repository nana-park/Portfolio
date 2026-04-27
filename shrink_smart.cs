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
                    int x = (orig.Width - nw) / 2;
                    int y = (orig.Height - nh) / 2;
                    
                    // Draw corners
                    Color tl = scaled.GetPixel(0, 0);
                    Color tr = scaled.GetPixel(nw - 1, 0);
                    Color bl = scaled.GetPixel(0, nh - 1);
                    Color br = scaled.GetPixel(nw - 1, nh - 1);
                    
                    g.FillRectangle(new SolidBrush(tl), 0, 0, x, y);
                    g.FillRectangle(new SolidBrush(tr), x + nw, 0, orig.Width - (x + nw), y);
                    g.FillRectangle(new SolidBrush(bl), 0, y + nh, x, orig.Height - (y + nh));
                    g.FillRectangle(new SolidBrush(br), x + nw, y + nh, orig.Width - (x + nw), orig.Height - (y + nh));
                    
                    // Draw edges by stretching 1-pixel lines
                    Rectangle topSrc = new Rectangle(0, 0, nw, 1);
                    Rectangle topDst = new Rectangle(x, 0, nw, y);
                    using (Bitmap topEdge = scaled.Clone(topSrc, scaled.PixelFormat)) { g.DrawImage(topEdge, topDst); }
                    
                    Rectangle botSrc = new Rectangle(0, nh - 1, nw, 1);
                    Rectangle botDst = new Rectangle(x, y + nh, nw, orig.Height - (y + nh));
                    using (Bitmap botEdge = scaled.Clone(botSrc, scaled.PixelFormat)) { g.DrawImage(botEdge, botDst); }
                    
                    Rectangle lSrc = new Rectangle(0, 0, 1, nh);
                    Rectangle lDst = new Rectangle(0, y, x, nh);
                    using (Bitmap lEdge = scaled.Clone(lSrc, scaled.PixelFormat)) { g.DrawImage(lEdge, lDst); }
                    
                    Rectangle rSrc = new Rectangle(nw - 1, 0, 1, nh);
                    Rectangle rDst = new Rectangle(x + nw, y, orig.Width - (x + nw), nh);
                    using (Bitmap rEdge = scaled.Clone(rSrc, scaled.PixelFormat)) { g.DrawImage(rEdge, rDst); }
                    
                    // Draw centered shrunk image
                    g.DrawImage(scaled, x, y);
                    
                    final.Save(outputFile, System.Drawing.Imaging.ImageFormat.Png);
                }
            }
        }
    }
}
