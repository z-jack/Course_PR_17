[b] = xlsread('mix.xlsx',1,'A1��D1628');
x = b(:,1);
y = b(:,2);
%c = b(:,3);
%�Ѿ������ݼ��������������ֱ��ȡǰ23����Ϊ����
data = [x(1:23,1),y(1:23,1)];
%���ڼ�¼�㵽�����ľ���
dist = zeros(1,23);
for k = 1:1000
%������¼�㱻�ֵ��Ǹ�����
c = zeros(1628,1);
sum = zeros(23,3);
for i = 1:1628
    for j = 1:23
        dist(1,j) = sqrt((x(i,1)-data(j,1))^2+(y(i,1)-data(j,2))^2);
    end
    [mi,index]=min(dist);
    c(i,1) = index;
    sum(c(i,1),1)=x(i)+sum(c(i,1),1);
    sum(c(i,1),2)=y(i)+sum(c(i,1),2);
    sum(c(i,1),3)=sum(c(i,1),3)+1;
end
%���¼����ֵ
for m = 1:23
    data(m,1) = sum(m,1)/sum(m,3);
    data(m,2) = sum(m,2)/sum(m,3);
end
end
%��ͼ
for i = 1:1628
    rand('seed',c(i,1));
    color = rand(1,3);
    plot(x(i,1),y(i,1),'*','color',color);
    hold on;
end    