class Solution:
    def nextGreaterElement(self, nums1, nums2):
        storage = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    k = j + 1
                    while k < len(nums2):
                        if nums2[j] < nums2[k]:
                            storage.append(nums2[k])
                            break
                        k += 1
                    else:
                        storage.append(-1)
        return storage